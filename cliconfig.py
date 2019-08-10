"""cliconfig.py - Configuration of constants for cli.py."""

# Imports

import lib.directory as directory


# Constants

METAVAR = '<command>'
"""How command argument shows in usage help."""

HELP = 'the command to run'
"""Description of the command supbarser (METAVAR) in help."""

DIRECTORIES = [
    directory.Directory('example', 'example command')
]
"""Directory objects for configured commands."""
