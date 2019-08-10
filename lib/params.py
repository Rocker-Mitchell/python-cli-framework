"""params.py - Class definition for parameter parser."""


class Params:
    """A base implementation and template for parameter parser subclasses."""

    def __init__(self, parser):
        """Initialize object.

        Args:
            parser (argparse.ArgumentParser): An empty parser to add arguments to and use for parsing.
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
