"""view.py - Class definition for views."""


class View:
    """A base implementation for view subclasses."""

    def set_attr(self, name, value):
        """Set an attribute on self for dependent print functions.

        Args:
            name (str): The name for the attribute.
            value: The value for the attribute.
        """
        setattr(self, name, value)
