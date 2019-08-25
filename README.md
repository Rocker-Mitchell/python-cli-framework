# python-cli-framework
A framework to organize code for a CLI program with commands

The script can be run in terminal: `python3 cli.py ...` with either the
help flag (-h) or the command name and its arguments. The 'example'
command is implemented to demo the script, and can be removed when
building your own commands.

## How to Implement Commands
Commands are available when explicitly defined in `cliconfig.py`, where
a collection of Directory objects store the command name, help dialogs,
and can resolve related file and class names.

With a command name defined, the code will load files/classes for
parsing, processing, and printing.

Parsing arguments is handled by paramparsers/\[*command*\]params.py which defines
\[*Command*\]Params, extended from the Params class.

Processing is handled by controllers/\[*command*\]controller.py which
defines \[*Command*\]Controller, extended from the Controller class.

Printing is handled by views/\[*command*\]view.py which defines
\[*Command*\]View, extended from the View class.
