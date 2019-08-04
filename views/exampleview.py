"""exampleview.py - An example view."""

# Imports

import lib.view as view


# View

class ExampleView(view.View):
    """View for example command."""

    # attributes
    foo = None
    bar = None

    def print(self):
        """Print the example view."""
        # validate attributes are set
        if self.foo is None or self.bar is None:
            raise ValueError('must set foo and bar in view')

        # print the values stored
        print('Parsed foo:', self.foo)
        print('Parsed bar:', self.bar)
