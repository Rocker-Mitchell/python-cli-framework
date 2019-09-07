"""exampleparams.py"""

# Imports

from pvc import ParamParser


# Params

class ExampleParser(ParamParser):
    """Parameter parser for example command."""

    def build_args(self):
        """Build arguments for example command."""
        # add commands to parser
        self.add_argument('--foo', action='store_true', help='foo flag')
        self.add_argument('bar', help='bar parameter')
