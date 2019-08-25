# Todo List

- [x] library
    - [x] directory class
        - organize/format command name, module/class names, and help dialog for `argparse`
        - [ ] allow custom module/class names to be set
    - [x] controller base class
        - template for subclass controllers
        - constructor to assign parser and view attributes
    - [x] view base class
        - template for subclass views
        - method to set attributes used in view
    - [x] params base class
        - template for subclass param parsers
        - handle argument parsing, return params

- [x] config file
    - holding list of directory objects, how to access command modules
    - [x] rename from directoryconfig.py for clarity of use; config for cli 

- [x] bootstrap file cli.py
    - [x] partial parse to determine command
        - use directory config for available commands
    - [x] dynamically import command modules and classes
    - construct command objects and initiate controller code
    
- [x] readme file
    - [x] summary
    - [x] how to use
