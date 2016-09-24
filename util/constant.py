"""Provide a decorator to create constants and classes for creating constants"""

from __future__ import absolute_import, division, unicode_literals, print_function


def constant(get_value):
    """Decorator to turn a function into a read-only property.

    This decorator/function dos NOT magically make the object immutable, so
    the value is not truly constant, but it does enforce a read-only binding.

    :param get_value: A callable that returns a value to make constant.
    :type get_value: callable
    :return: A read-only property producing the value returned by get_value()
    :rtype: property

    :Example:

    >>> class Constants(object):
    ...     @constant
    ...     def VAL():
    ...         return 42
    ...
    >>> const = Constants()
    >>> const.VAL
    42
    >>> const.VAL = 0
    Traceback (most recent call last):
        ...
    TypeError: value is read-only

    """

    # Define the property getter
    def getter(self):
        """Property getter for a constant. Retrieves the constant value."""
        return get_value()

    # Prevent setting values, raise TypeError instead
    def setter(self, value):
        """Property setter for a constant. Does not allow values to be set."""
        raise TypeError('value is read-only')

    # Create a property from the above functions
    return property(getter, setter)
