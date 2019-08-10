"""errormessages.py - Functions to format error messages for parser errors."""


def attr_error(attribute, message, value=None, hint=None):
    """Format an error string for parser errors.

    The string format will look like:
    'attribute [attribute]: [message]: [value] ([hint])'

    Args:
        attribute (str): The attribute causing error.
        message (str): The error message.
        value: The value of the attribute. Will format with repr(value). Defaults to not adding to return string.
        hint (str): The hint for the error. Defaults to not adding to return string.
    """
    output = 'attribute ' + attribute + ': ' + message

    if value is not None:
        output += ': ' + repr(value)

    if hint is not None:
        output += ' (' + hint + ')'

    return output
