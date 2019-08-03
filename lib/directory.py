"""directory.py - Class definition for directory entries."""


# Class

class Directory:
    """A container for directory information."""

    def __init__(self, command):
        """Initialize object.

        Args:
            command (str): The name of the command.
        """
        self.command = command

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
            str: The formatted string.
        """
        return self.command.capitalize() + 'View'
