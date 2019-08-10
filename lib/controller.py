"""controller.py - Class definition for controllers."""


class Controller:
    """A base implementation and template for controller subclasses."""

    def __init__(self, view):
        """Initialize object.

        Args:
            view (lib.view.View): The view for the controller.
        """
        self.view = view

    def main(self, params):
        """Run controller's main code.

        Args:
            params (argparse.Namespace): The parsed params.
        """
        raise NotImplementedError('main() must be implemented.')
