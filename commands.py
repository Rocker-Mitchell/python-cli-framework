"""commands.py - Configuration of commands for cli.py."""


# Directory class

class Directory:
    """A container for directory information about commands."""

    def __init__(self, command, help_str):
        """Initialize object.

        Args:
            command (str): The name of the command.
            help_str (str): The help string for the command.
        """
        self.command = command
        self.help = help_str

    def params_module_name(self):
        """Get the command's param parser module name.

        Returns:
            str: The formatted name.
        """
        return self.command + 'params'

    def params_class_name(self):
        """Get the command's param parser class name.

        Returns:
            str: The formatted name.
        """
        return self.command.capitalize() + 'Params'

    def controller_module_name(self):
        """Get the command's controller module name.

        Returns:
            str: The formatted name.
        """
        return self.command + 'controller'

    def controller_class_name(self):
        """Get the command's controller class name.

        Returns:
            str: The formatted name.
        """
        return self.command.capitalize() + 'Controller'

    def view_module_name(self):
        """Get the command's view module name.

        Returns:
            str: The formatted name.
        """
        return self.command + 'view'

    def view_class_name(self):
        """Get the command's view class name.

        Returns:
            str: The formatted name.
        """
        return self.command.capitalize() + 'View'


# Command Directory list

DIRECTORIES = [
    Directory('example', 'example command')
]
"""Directory objects for configured commands."""
