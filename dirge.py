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

from docopt import docopt
from os import mkdir

from parse.paths import determine_paths
from util.compat import eprint


def dirge(template, simulate=False, verbose=False):
    """Generates directories based on a template file.

    :param template: Filename of template that provides generation rules
    :param simulate: If True, no directories will be created, paths printed
    :param verbose: If True, print paths as directories are created
    :type template: str
    :type simulate: bool
    :type verbose: bool

    """

    with open(template) as f:
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
