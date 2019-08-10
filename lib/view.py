"""view.py - Class definition for views."""


class View:
    """A base implementation for view subclasses.

    A print function isn't required here as views may have different contexts for printing (i.e. prompts for interactive
    input, progress bars, debug messages) which should be implemented by those subclasses.
    """

    def set_attr(self, name, value):
        """Set an attribute on self.

        Subclasses should use attributes for dynamic content to print. Errors should raise if an attribute was not set
        or is the wrong type, but shouldn't error from the data itself.

        Args:
            name (str): The name for the attribute.
            value: The value for the attribute.
        """
        setattr(self, name, value)
