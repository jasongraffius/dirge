"""Provide helper functions for compatibility between python 2 and python 3"""

from __future__ import absolute_import, division, unicode_literals, print_function
import sys


def is_str(obj):
    """Determine if an object is string-like or a string.

    Intended to be cross compatible with python 2 and 3

    :param obj: Object to test if it is a string or string-like object
    :type obj: str, ...
    :return: True if the object is a string or inherits from the base string class for a given version
    :rtype: bool

    :Example:

    >>> is_str([1, 2, 3])
    False
    >>> is_str('this is a string')
    True
    >>> is_str(5)
    False
    >>> is_str({'a', 'b', 'c'})
    False
    >>> is_str('')
    True

    """

    try:
        # Attempt to try python-2 style
        # noinspection PyCompatibility
        return isinstance(obj, basestring)
    except NameError:
        # If basestring failed, try assuming python-3
        return isinstance(obj, str)


def eprint(*args, **kwargs):
    """Print an error message to stderr.

    Functions exactly like print, but prints to stderr instead of stdout.

    :param args: positional arguments to pass to print
    :param kwargs: keyword args to pass to print. Don't use file.
    :type args: list
    :type kwargs: dict

    """
    print(*args, file=sys.stderr, **kwargs)
