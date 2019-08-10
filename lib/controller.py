"""controller.py - Class definition for controllers."""


class Controller:
    """A base implementation and template for controller subclasses."""

    def __init__(self, parser, view):
        """Initialize object.

        Args:
            parser (argparse.ArgumentParser): The parser for the controller.
            view (lib.view.View): The view for the controller.
        """
        self.parser = parser
        self.view = view

    def main(self, args):
        """Run controller's main code.

        Args:
            args (list[str]): A list of argument strings.
        """
        raise NotImplementedError('main() must be implemented.')
