"""cli.py - Bootstrap script; parses command line arguments to run related commands."""

# Imports

import argparse
import importlib
import commands


# Constants

METAVAR = '<command>'
"""How command argument shows in usage help."""

HELP = 'the command to run'
"""Description of the command subparser (METAVAR) in help."""


# Functions

def main(args=None):
    """Run main code.

    Args:
        args (list[str]): List of strings to parse. Defaults to using sys.argv.
    """
    # build parser to obtain command
    parser = argparse.ArgumentParser()

    command_subparser = parser.add_subparsers(dest='command', metavar=METAVAR, required=True, help=HELP)

    # from the command config, build command parsers
    command_dir_parser = dict()
    for directory in commands.DIRECTORIES:
        # remove help flag as we won't have controller arguments' help strings yet
        command_parser = command_subparser.add_parser(directory.command, help=directory.help,
                                                      description=directory.description, add_help=False)

        # track directories and parsers by command name
        command_dir_parser[directory.command] = (directory, command_parser)

    namespace, extra_args = parser.parse_known_args(args)

    # attempt to import the parsed command
    directory, command_parser = command_dir_parser[namespace.command]
    try:
        params_module = importlib.import_module('paramparsers.' + directory.params_module_name())
        controller_module = importlib.import_module('controllers.' + directory.controller_module_name())
        view_module = importlib.import_module('views.' + directory.view_module_name())
    except ModuleNotFoundError:
        error = attr_error_message(METAVAR, 'could not import modules for command', namespace.command,
                                   "the module files may not have been created, or the module names don't match what "
                                   "was expected")
        parser.error(error)
        return

    # try to import classes
    try:
        params_class = getattr(params_module, directory.params_class_name())
        controller_class = getattr(controller_module, directory.controller_class_name())
        view_class = getattr(view_module, directory.view_class_name())
    except AttributeError:
        error = attr_error_message(METAVAR, 'could not load classes from modules for command', namespace.command,
                                   "the code may not have been implemented, or the class names don't match what was "
                                   "expected")
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


def attr_error_message(attribute, message, value=None, hint=None):
    """Format an error message for parser errors.

    The string format will look like:
    'attribute [attribute]: [message]: [value] ([hint])'

    Args:
        attribute (str): The attribute causing the error.
        message (str): The error message.
        value: The value of the attribute, which will be formatted with repr(value). Defaults to None to not add to the
            formatted string.
        hint (str): The hint for the error. Defaults to None to not add to the formatted string.
    """
    message = 'attribute ' + attribute + ': ' + message

    if value is not None:
        message += ': ' + repr(value)

    if hint is not None:
        message += ' (' + hint + ')'

    return message


# Script

if __name__ == '__main__':
    main()
