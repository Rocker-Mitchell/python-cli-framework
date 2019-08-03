# Bootstrap file

- [ ] library
    - [ ] directory class
        - organize/format command name, module/class names, and help dialog for `argparse`
    - [ ] controller base class
        - template for subclass controllers
        - constructor to assign parser and view attributes
    - [ ] view base class
        - template for subclass views
        - method to set attributes used in view

- [ ] config file directory.py
    - holding list of directory objects

- [ ] bootstrap file cli.py
    - [ ] partial parse to determine command
        - use directory config for available commands
    - [ ] dynamically import controller and view classes
    - construct controller/view objects and initiate controller code
