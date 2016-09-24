"""Provide a decorator to create constants and classes for creating constants"""

from __future__ import absolute_import, division, unicode_literals, print_function


def constants(cls):
    """Decorator to convert all members of a class to read-only.

    This decorator/function dos NOT magically make the objects immutable, so
    the values are not truly constant, but it does enforce a read-only
    binding, which is good enough for most uses. Note that no values can be
    added to the class after its definition either.

    :param cls: A class to make constant
    :type cls: type
    :return: A read-only object of type cls
    :rtype: cls

    :Example:

    >>> @constants
    ... class Const(object):
    ...     VAL = 42
    ...
    >>> Const.VAL
    42
    >>> Const.VAL = 0
    Traceback (most recent call last):
        ...
    TypeError: value is read-only

    """
    pass
