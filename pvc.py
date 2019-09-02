"""pvc.py - Base class definitions for parser, view, and controller objects."""


# Classes

class ParamParser:
    """A base implementation for parameter parser subclasses."""

    def __init__(self, parser):
        """Initialize object.

        Args:
            parser (argparse.ArgumentParser): An empty argument parser to add arguments to and use for parsing.
        """
        self.parser = parser

    def parse_args(self, args):
        """Parse given arguments into parameters.

        Args:
            args (list[str]): List of argument strings.

        Returns:
            argparse.Namespace: The parameters parsed.
        """
        raise NotImplementedError('parse_args() must be implemented')


class View:
    """A base implementation for view subclasses.

    A print function isn't required in the base as views may have different contexts for printing (i.e. prompts for
    interactive input, progress bars, debug messages) which should be implemented by those subclasses.
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


class Controller:
    """A base implementation for controller subclasses."""

    def __init__(self, view):
        """Initialize object.

        Args:
            view (View): The view for the controller.
        """
        self.view = view

    def main(self, params):
        """Run controller's main code.

        Args:
            params (argparse.Namespace): The parsed params.
        """
        raise NotImplementedError('main() must be implemented.')
