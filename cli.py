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

    command_subparser = parser.add_subparsers(dest='command', metavar='<command>', required=True)

    # from the directory config, add commands
    commands = dict()
    for directory in directoryconfig.DIRECTORIES:
        # remove help flag as we won't have controller arguments' help strings yet
        command_parser = command_subparser.add_parser(directory.command, help=directory.help, add_help=False)

        # track directories and parsers under command name
        commands[directory.command] = (directory, command_parser)

    namespace, extra_args = parser.parse_known_args(args)

    # attempt to import the parsed command
    directory, command_parser = commands[namespace.command]
    try:
        params_module = importlib.import_module('paramparsers.' + directory.params_module_name())
        controller_module = importlib.import_module('controllers.' + directory.controller_module_name())
        view_module = importlib.import_module('views.' + directory.view_module_name())
    except ModuleNotFoundError:
        error = errormessages.attr_error('<command>', 'could not import modules for command', namespace.command,
                                         "the module files may not have been created, or the module names don't match "
                                         "what was expected")
        parser.error(error)
        return

    # try to import classes
    try:
        params_class = getattr(params_module, directory.params_class_name())
        controller_class = getattr(controller_module, directory.controller_class_name())
        view_class = getattr(view_module, directory.view_class_name())
    except AttributeError:
        error = errormessages.attr_error('<command>', 'could not load classes from modules for command',
                                         namespace.command,
                                         "the code may not have been implemented, or the class names don't match what "
                                         "was expected")
        parser.error(error)
        return

    # add back help flag
    command_parser.add_argument('-h', '--help', action='help', help='show this help message and exit')

    # parse params
    params = params_class(command_parser)
    parsed_params = params.parse_args(extra_args)

    # construct view/controller and run controller code
    view = view_class()
    controller = controller_class(view)
    controller.main(parsed_params)


# Script

if __name__ == '__main__':
    main()
