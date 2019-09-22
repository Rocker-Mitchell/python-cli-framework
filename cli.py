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

PARSER_PACKAGE = 'paramparsers'
"""The package containing command parameter parsers."""

VIEW_PACKAGE = 'views'
"""The package containing command views."""

CONTROLLER_PACKAGE = 'controllers'
"""The package containing command controllers."""


# Functions

def _get_module_attr(module_name, attribute_name):
    """Import a module and get an attribute from it.

    Args:
        module_name (str): The module name.
        attribute_name (str): The attribute name.

    Returns:
        Any: The attribute.

    Raises:
        ModuleNotFoundError: The module could not be imported.
        AttributeError: The attribute could not be found in the module.
    """
    module = importlib.import_module(module_name)
    attribute = getattr(module, attribute_name)
    return attribute


def main(args=None):
    """Run main code.

    Args:
        args (list[str]): List of strings to parse. Defaults to using sys.argv.
    """
    # build parser to contain command-specific parsers
    parser = argparse.ArgumentParser()
    command_subparsers = parser.add_subparsers(dest='command', metavar=METAVAR, required=True, help=HELP)

    # from the commands config, build command parsers
    command_dict = dict()
    for directory in commands.DIRECTORIES:
        # load command's param parser; build arguments
        param_parser_class = _get_module_attr(PARSER_PACKAGE + '.' + directory.params_module_name,
                                              directory.params_class_name)
        param_parser = param_parser_class()

        # create subparser; use param_parser to build arguments
        command_parser = command_subparsers.add_parser(directory.command, help=param_parser.help,
                                                       description=param_parser.description, epilog=param_parser.epilog)
        param_parser.build_args(command_parser)

        # track directories and parsers by command name
        command_dict[directory.command] = {'directory': directory, 'param': param_parser, 'parser': command_parser}

    namespace = parser.parse_args(args)
    # TODO unrecognized arguments are erroring from main parser rather than the command parser

    # run validation from param parser
    param_parser = command_dict[namespace.command]['param']
    error_msg = param_parser.validate(namespace)
    if error_msg is not None:
        command_parser = command_dict[namespace.command]['parser']
        command_parser.error(error_msg)  # this includes the command name in the usage string

    # load classes for the parsed command
    directory = command_dict[namespace.command]['directory']
    view_class = _get_module_attr(VIEW_PACKAGE + '.' + directory.view_module_name, directory.view_class_name)
    controller_class = _get_module_attr(CONTROLLER_PACKAGE + '.' + directory.controller_module_name,
                                        directory.controller_class_name)

    # construct view/controller and run controller code
    view = view_class()
    controller = controller_class(view)
    controller.main(namespace)


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
