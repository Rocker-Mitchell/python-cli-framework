"""commands.py - Configuration of commands for cli.py."""


# Directory class

class Directory:
    """A container for directory information about commands."""

    def __init__(self, command):
        """Initialize object.

        Args:
            command (str): The name of the command.
        """
        self.command = command

        capitalized = command.capitalize()

        self.params_module_name = command + 'params'
        self.params_class_name = capitalized + 'Parser'

        self.view_module_name = command + 'view'
        self.view_class_name = capitalized + 'View'

        self.controller_module_name = command + 'controller'
        self.controller_class_name = capitalized + 'Controller'


# Command Directory list

DIRECTORIES = [
    Directory('example')
]
"""Directory objects for configured commands."""
