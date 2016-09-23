#!/usr/bin/env python
"""Dirge - Directory generator"""

from __future__ import absolute_import, division, unicode_literals, print_function


def determine_paths(read, parent=None):
    """Determines the list of paths to create from a directory specification

    :param read: text to parse for generation rules
    :type read: str, file
    :return: list of paths that should be generated
    :rtype: list

    :Example with string:

    >>> text = '''
    ...
    ... path
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
    ... dir_one
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
