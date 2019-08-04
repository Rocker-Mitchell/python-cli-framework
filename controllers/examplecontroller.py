"""examplecontroller.py - An example controller."""

# Imports


import lib.controller as controller


# Controller

class ExampleController(controller.Controller):
    """Controller for example command."""

    def main(self, args):
        """Run example command code.

        Args:
            args (list[str]): A list of argument strings.
        """
        # add commands to parser
        self.parser.add_argument('--foo', action='store_true', help='foo flag')
        self.parser.add_argument('bar', help='bar parameter')

        namespace = self.parser.parse_args(args)

        # update view with the parsed attributes
        self.view.set_attr('foo', namespace.foo)
        self.view.set_attr('bar', namespace.bar)

        self.view.print()
