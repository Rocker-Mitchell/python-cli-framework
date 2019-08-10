# Todo Points

- [x] library
    - [x] directory class
        - organize/format command name, module/class names, and help dialog for `argparse`
    - [x] controller base class
        - template for subclass controllers
        - constructor to assign parser and view attributes
    - [x] view base class
        - template for subclass views
        - method to set attributes used in view

- [x] config file directory.py
    - holding list of directory objects

- [x] bootstrap file cli.py
    - [x] partial parse to determine command
        - use directory config for available commands
    - [x] dynamically import controller and view classes
    - construct controller/view objects and initiate controller code
