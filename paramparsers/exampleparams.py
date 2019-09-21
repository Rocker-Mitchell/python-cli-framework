"""exampleparams.py - An example param parser."""

# Imports

from pvc import ParamParser


# Params

class ExampleParser(ParamParser):
    """Parameter parser for example command."""

    def build_args(self, parser):
        """Build arguments for example command."""
        parser.add_argument('--foo', action='store_true', help='foo flag')
        parser.add_argument('bar', help="bar parameter; pass 'error' to force parser failure")

    def validate(self, namespace):
        """Validate arguments for example command."""
        if namespace.bar.lower() == 'error':
            return 'A validation error occurred'
