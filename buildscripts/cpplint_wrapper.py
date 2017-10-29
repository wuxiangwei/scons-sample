#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys
import cpplint


_EXTENSIONS = [ 'cc', 'cxx', 'cpp', 'c', 'hpp', 'h' ]

def check_extension(filename):
    pos = filename.rfind('.')

    if -1 == pos:
        ret = False
    else:
        filetx = filename[pos+1:]
        ret = filetx in _EXTENSIONS

    return ret


def get_source_files(prefix):
    source_files = []

    if os.path.isfile(prefix):
        if check_extension(prefix):
            source_files.append(prefix)
        return source_files

    for root, dirs, files in os.walk(prefix):
        root_files = [ os.path.join(root, filename) for filename in files \
                if check_extension(filename) ]
        source_files.extend(root_files)

    return source_files


def do_lint(paths):
    source_files = []
    for path in paths:
        files = get_source_files( path )
        source_files.extend(files)

    if not source_files:
        print('No files!')
        return

    opts = [
        '--extensions=' + ','.join(_EXTENSIONS),
        '--counting=detailed'
    ]

    filenames = cpplint.ParseArguments(opts+source_files)
    for filename in filenames:
        cpplint.ProcessFile( filename, cpplint._cpplint_state.verbose_level)

    print('='*80)
    cpplint._cpplint_state.PrintErrorCounts()
    print('='*80)
    sys.exit(cpplint._cpplint_state.error_count > 0)
