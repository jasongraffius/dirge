#!/usr/bin/env python
"""Dirge - Directory generator"""

from __future__ import absolute_import, division, unicode_literals, print_function


def _is_str(obj):
    """Determine if an object is string-like or a string.

    Intended to be cross compatible with python 2 and 3

    :param obj: Object to test if it is a string or string-like object
    :type obj: str, ...
    :return: True if the object is a string or inherits from the base string class for a given version
    :rtype: bool

    :Example:

    >>> _is_str([1, 2, 3])
    False
    >>> _is_str('this is a string')
    True
    >>> _is_str(5)
    False
    >>> _is_str({'a', 'b', 'c'})
    False
    >>> _is_str('')
    True

    """

    try:
        # Attempt to try python-2 style
        # noinspection PyCompatibility
        return isinstance(obj, basestring)
    except NameError:
        # If basestring failed, try assuming python-3
        return isinstance(obj, str)


def parse_line(line):
    """Parses a single line of a directory specification.

    This function should search a line for a directory name, and then return that name and its indent length

    :param line: Line to parse
    :type line: str
    :return: A tuple containing the directory name and the level of the directory
    :rtype: tuple

    :Example:

    >>> parse_line(' | | +-directory')
    ('directory', 6)
    >>> parse_line('-root')
    ('root', 0)
    >>> parse_line('        deep-folder')
    ('deep-folder', 8)
    >>> parse_line('-----> folder')
    ('folder', 7)
    """
    pass


def determine_paths(read, parent=None):
    """Determines the list of paths to create from a directory specification

    :param read: Text to parse for generation rules
    :type read: str, file
    :return: A list of paths that should be generated
    :rtype: list

    :Example with string:

    >>> text = '''
    ...
    ... -path
    ...   |
    ...   +-along
    ...   |  |
    ...   |  +-the
    ...   |  |
    ...   |  +-way
    ...   |  |
    ...   |  `-down
    ...   |
    ...   `-for
    ...      |
    ...      `-dirs
    ...
    ... '''
    >>> paths = determine_paths(text)
    >>> paths == [
    ...     'path',
    ...     'path/along',
    ...     'path/along/down',
    ...     'path/along/the',
    ...     'path/along/way',
    ...     'path/for',
    ...     'path/for/dirs',
    ... ]
    True

    :Example with absolute paths:

    >>> text = '''
    ... -dir_one
    ...   +-dir_two
    ...   `-dir_three
    ... '''
    >>> paths = determine_paths(text, "/parent/directory/path")
    >>> paths == [
    ...     '/parent/directory/path/dir_one',
    ...     '/parent/directory/path/dir_one/dir_two',
    ...     '/parent/directory/path/dir_one/dir_three',
    ... ]
    True
    """
    pass


def main():
    pass


if __name__ == '__main__':
    main()
