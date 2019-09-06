# python-cli-framework
A framework to organize code for a CLI program with commands

The script can be run in terminal: `python3 cli.py ...` with either the
help flag (-h) or the command name and its arguments. The 'example'
command is implemented to demo the script, and can be removed when
building your own commands.

## How to Implement Commands
Commands are available when explicitly defined in
`commands.DIRECTORIES`, where a collection of Directory objects store
the command name, help dialogs, and can resolve related file and class
names.

With a command name defined, the code will load files/classes for
parsing, processing, and printing.

- Parsing arguments is handled by the
`paramparsers.[command]params.[Command]Params` class, which extends the
`pvc.ParamParser` class. The parser class must implement
`parse_args(args)`, adding arguments to `self.parser` and using it to
parse args and return results.

- Printing is handled by the `views.[command]view.[Command]View` class,
which extends the `pvc.View` class. The view class can flexibly
implement functions to print, depending on needs (i.e. progress bars,
input prompts, etc.).

- Processing is handled by the
`controllers.[command]controller.[Command]Controller` class, which
extends the `pvc.Controller` class. The controller class must implement
`main(params)`, taking results from the parser class, do processing,
modifying the view by `self.view.set_attr(name, value)` and calling
print functions defined in the view class.
