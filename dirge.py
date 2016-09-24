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
        return m.group(3), len(m.group(1))  # Return the values
    else:  # Otherwise, no match
        return (None, 0)  # Return None


def create_full_path(path_stack, name, depth):
    """Creates a full path from the name, level and current stack.

    Walks back up path_stack until a lower level path is found. A fully
    qualified path is returned. The stack is not modified, but the resulting
    value should be appended to the stack before the next invocation of this
    function.

    :param path_stack: A stack of directory paths and their 'level'
    :param name: The name of the directory to insert into the tree
    :param depth: The 'depth' or 'level' of the new directory
    :type path_stack: list
    :type name: str
    :type depth: int
    :return: Full path of new directory, or None if there are no parents
    :rtype: str, None

    :Example:

    >>> # Stack representing dirs a/b a/c/d
    >>> stack = [
    ...     ('a', 0),
    ...     ('a/b', 2),
    ...     ('a/c', 2),
    ...     ('a/c/d', 4),
    ... ]
    >>> create_full_path(stack, 'e', 6) == 'a/c/d/e'
    True
    >>> create_full_path(stack, 'f', 4) == 'a/c/f'
    True
    >>> create_full_path(stack, 'g', 2) == 'a/g'
    True
    >>> create_full_path(stack, 'h', 0) is None
    True

    """
    pass


def determine_paths(read, parent=None):
    """Determines the list of paths to create from a directory specification

    :param read: Text to parse for generation rules
    :param parent: Parent directory/prefix to append to each generated directory
    :type read: str, file
    :type parent: str
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
