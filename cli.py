"""cli.py - Bootstrap script; parses command line arguments to run related commands."""

# Imports

import argparse
import importlib
import lib.errormessages as errormessages
import directoryconfig


# Functions

def main(args=None):
    """Run main code.

    Args:
        args (list[str]): List of strings to parse. Defaults to using sys.argv.
    """
    # build parser to obtain command
    parser = argparse.ArgumentParser()

    commands = parser.add_subparsers(dest='command', metavar='<command>')

    # from the directory config, add commands
    controller_parsers = dict()
    for directory in directoryconfig.DIRECTORIES:
        # remove help flag as we won't have controller arguments' help strings yet
        command_parser = commands.add_parser(directory.command, help=directory.help, add_help=False)

        # track parsers under command name
        controller_parsers[directory.command] = command_parser

    namespace, extra_args = parser.parse_known_args(args)

    # attempt to import the parsed command
    directory = directoryconfig.DIRECTORIES[namespace.command]
    try:
        controller_module = importlib.import_module('.' + directory.controller_module_name(), 'controllers')
        view_module = importlib.import_module('.' + directory.view_module_name(), 'views')
    except ModuleNotFoundError:
        error = errormessages.attr_error('<command>', 'could not import modules for command', namespace.command,
                                         "the module files may not have been created, or the module names don't match "
                                         "what was expected")
        parser.error(error)
        return

    # try to import classes
    try:
        controller_class = getattr(controller_module, directory.controller_class_name())
        view_class = getattr(view_module, directory.view_class_name())
    except AttributeError:
        error = errormessages.attr_error('<command>', 'could not load classes from modules for command',
                                         namespace.command,
                                         "the code may not have been implemented, or the class names don't match what "
                                         "was expected")
        parser.error(error)
        return

    # retrieve the related command parser and add back help flag
    command_parser = controller_parsers[namespace.command]
    command_parser.add_argument('-h', '--help', action='help')

    # construct view/controller and run controller code
    view = view_class()
    controller = controller_class(command_parser, view)
    controller.main(extra_args)


# Script

if __name__ is '__main__':
    main()
