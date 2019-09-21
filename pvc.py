"""pvc.py - Base class definitions for parser, view, and controller objects."""


# Classes

class ParamParser:
    """A base implementation for parameter parser subclasses."""

    # TODO move command help and description strings to be members of param parser

    def build_args(self, parser):
        """Build arguments for parameter parsing.

        Subclasses should add arguments as needed, with help strings defined for usage.

        Args:
            parser (argparse.ArgumentParser): A parser object used for parsing.
        """
        raise NotImplementedError('build_args() must be implemented')

    def validate(self, namespace):
        """Validate arguments from parameter parsing.

        Subclasses can implement this function to handle input requirements more complicated than can be added to the
        parser.

        Args:
            namespace (argparse.Namespace): The namespace after parsing.

        Returns:
            str|None: An error message if validation fails.
        """
        pass


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

        Subclasses should process the params, do work, and call self.view to print to console.

        Args:
            params (argparse.Namespace): The parsed params.
        """
        raise NotImplementedError('main() must be implemented.')
