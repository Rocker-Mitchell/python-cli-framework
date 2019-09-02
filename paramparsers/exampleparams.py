"""exampleparams.py"""

# Imports

from pvc import ParamParser


# Params

class ExampleParams(ParamParser):
    """Parameter parser for example command."""

    def parse_args(self, args):
        """Parse given arguments into parameters.

        Args:
            args (list[str]): List of argument strings.

        Returns:
            argparse.Namespace: The parameters parsed.
        """
        # add commands to parser
        self.parser.add_argument('--foo', action='store_true', help='foo flag')
        self.parser.add_argument('bar', help='bar parameter')

        namespace = self.parser.parse_args(args)
        return namespace
