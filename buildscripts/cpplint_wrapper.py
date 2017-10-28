#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import cpplint


def get_source_files( prefix ):
    source_files = []

    def is_cxx_file( path ):
        suffix = [ 'cc', 'cpp', 'c', 'hpp', 'h' ]
        splited = path.split( '.' )
        return True if len(splited) >= 2 and splited[-1] in suffix else False

    if os.path.isfile( prefix ):
        if is_cxx_file( path ):
            source_files.append( prefix )
        return source_files

    for root, dirs, files in os.walk( prefix ):
        root_files = [ os.path.join( root, filename ) for filename in files \
            if is_cxx_file(filename) ]
        source_files.extend(root_files)

    return source_files


def run( paths ):
    source_files = []
    for path in paths:
        files = get_source_files( path )
        source_files.extend( files )

    never = [
        '-legal/copyright',
    ]

    filters = never
    args = [
        '--linelength=100',
        '--filter=' + ','.join( filters ),
        '--counting=detailed' ] + source_files

    filenames = cpplint.ParseArguments( args )
    for filename in filenames:
        cpplint.ProcessFile( filename, cpplint._cpplint_state.verbose_level)
    cpplint._cpplint_state.PrintErrorCounts()


if __name__ == '__main__':
    paths = []
    paths.append( "src/test/" )
    run( paths )
