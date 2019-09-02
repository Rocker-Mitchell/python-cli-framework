"""examplecontroller.py - An example controller."""

# Imports

from pvc import Controller


# Controller

class ExampleController(Controller):
    """Controller for example command."""

    def main(self, params):
        """Run example command code.

        Args:
            params (argparse.Namespace): The parsed params.
        """
        # update view with the parsed attributes
        self.view.set_attr('foo', params.foo)
        self.view.set_attr('bar', params.bar)

        self.view.print()
