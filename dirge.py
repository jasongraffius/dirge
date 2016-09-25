#!/usr/bin/env python
"""Dirge - Directory generator

Usage:
    dirge [options] <template>

Options:
    -s --simulate
        Simulate output. Don't create any directories, but print the paths to
        stdout.

    -v --verbose
        Verbose. Print each directory's path to stdout as it is generated.

"""

from __future__ import absolute_import, division, unicode_literals, print_function

import errno
import re

from docopt import docopt
from io import StringIO
from os import path, mkdir

from util.compat import is_str, eprint
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
        return None, 0  # Return None


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

    >>> from os import path
    >>> stack = [
    ...     (path.join('a'), 0),
    ...     (path.join('a', 'b'), 2),
    ...     (path.join('a', 'c'), 2),
    ...     (path.join('a', 'c', 'd'), 4),
    ... ]
    >>> create_full_path(stack, 'e', 6) == path.join('a', 'c', 'd', 'e')
    True
    >>> create_full_path(stack, 'f', 4) == path.join('a', 'c', 'f')
    True
    >>> create_full_path(stack, 'g', 2) == path.join('a', 'g')
    True
    >>> create_full_path(stack, 'h', 0) == 'h'
    True

    """

    # Walk up through path stack
    for d_name, d_level in reversed(path_stack):
        if depth <= d_level:
            continue  # Not a parent directory, either sibling or cousin

        # Found the next parent directory
        return path.join(d_name, name)

    # No parent found
    return None


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
    ...     path.join('path', 'along'),
    ...     path.join('path', 'along', 'down'),
    ...     path.join('path', 'along', 'the'),
    ...     path.join('path', 'along', 'way'),
    ...     path.join('path', 'for'),
    ...     path.join('path', 'for', 'dirs'),
    ... ]
    True

    :Example with absolute paths:

    >>> text = '''
    ... -dir_one
    ...   +-dir_two
    ...   `-dir_three
    ... '''
    >>> parent = path.join('parent', 'directory', 'path')
    >>> paths = determine_paths(text, parent)
    >>> paths == [
    ...     path.join(parent, 'dir_one'),
    ...     path.join(parent, 'dir_one', 'dir_three'),
    ...     path.join(parent, 'dir_one', 'dir_two'),
    ... ]
    True
    """

    # Read strings from a file-like interface
    if is_str(read):
        read = StringIO(read)

    # If there is no parent, the prefix is ''
    if parent is None:
        parent = ''

    # Keep track of paths generated
    paths = list()
    # Keep track of directory levels
    parent_stack = list()

    # Iterate over each line in the file/string
    for line in read:

        # Discard the trailing newline
        if len(line) > 0 and line[-1] == '\n':
            line = line[:-1]

        # Parse the line for the directory and its offset
        name, depth = parse_line(line)

        # If the line does not contain a directory, continue to the next line
        if name is None:
            continue

        # Find the path
        full_path = create_full_path(parent_stack, name, depth)

        # If there is no existing parent, create a new root-level directory
        if full_path is None:
            full_path = path.join(parent, name)

        # Keep the new path
        paths.append(full_path)
        # Update the stack
        parent_stack.append((full_path, depth))

    paths.sort()  # This is intended to keep them in an unambiguous order

    return paths


def dirge(template, simulate=False, verbose=False):
    """Generates directories based on a template file.

    :param template: Filename of template that provides generation rules
    :param simulate: If True, no directories will be created, paths printed
    :param verbose: If True, print paths as directories are created
    :type template: str
    :type simulate: bool
    :type verbose: bool

    """

    f = open(template)
    paths = determine_paths(f)

    if simulate:
        for path in paths:
            print(path)
    else:
        for path in paths:
            try:
                mkdir(path)
                if verbose:
                    print(path)
            except OSError as e:
                if e.errno == errno.EEXIST:
                    eprint('"' + path + '"', 'exists, skipping...')


def main():
    """Main entry point to the program.

    Grabs the command line arguments and calls dirge() to handle the parsing
    and generation.
    """

    # Get user arguments
    args = docopt(__doc__)
    dirge_args = dict()

    # Map command line args to function parameters
    expected_options = {
        '<template>': 'template',
        '--simulate': 'simulate',
        '--verbose': 'verbose',
    }

    # Extract function parameters from command line
    for option in expected_options:
        if option in args:
            # Convert each argument
            dirge_args[expected_options[option]] = args[option]

    # Start dirge
    dirge(**dirge_args)


if __name__ == '__main__':
    main()
