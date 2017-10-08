#!/usr/bin/env python
# coding:utf-8

import os
import sys


def usage():    
    prog = os.path.basename(sys.argv[0])
    print '%s all       -- build all' % prog
    print '%s clean     -- clean all' % prog


def main():
    if len(sys.argv) != 2:
        usage()
        sys.exit(0)
    
    command = ''
    if sys.argv[1] == 'all':
        command = ' '
    elif sys.argv[1] == 'clean':
        command = ' -c'

    if os.system('scons'+command):
        print 'build failed!!'


if __name__ == '__main__':
    main()
