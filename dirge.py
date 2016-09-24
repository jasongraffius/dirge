#!/usr/bin/env python
"""Dirge - Directory generator"""

from __future__ import absolute_import, division, unicode_literals, print_function

import re
from util.constants import constants

@constants
class Const(object):
    DIR_LINE_REGEX = re.compile(r"(\W*?)([-]+)?(\w[^|/\\?:<>]*)")

def parse_line(line):
    """Parses a single line of a directory specification.

    This function should search a line for a directory name, and then return that name and its indent length

    :param line: Line to parse
    :type line: str
    :return: A tuple containing the directory name and the level of the directory
    :rtype: tuple

    :Example:

    >>> parse_line(' | | +-directory') == ('directory', 6)
    True
    >>> parse_line('-root') == ('root', 0)
    True
    >>> parse_line('        deep-folder') == ('deep-folder', 8)
    True
    >>> parse_line('-----> folder') == ('folder', 7)
    True

    """

    # Parse the line with a regex
    m = Const.DIR_LINE_REGEX.match(line)

    if m:  # If the regex matched
        return (m.group(3), len(m.group(1)))  # Return the values
    else:  # Otherwise, no match
        return (None, 0)  # Return None


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
