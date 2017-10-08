#!/usr/bin/env python
# coding:utf-8

import os
import sys

SCONS_VERSION = os.environ.get('SCONS_VERSION', '3.0.0')

project_root = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
scons_dir = os.path.join(
    project_root, 'third_party', 'scons-' + SCONS_VERSION, 'scons-local-' + SCONS_VERSION)

if not os.path.exists(scons_dir):
    print "Could not find SCons in '%s'" % scons_dir
    sys.exit(1)

sys.path = [scons_dir] + sys.path

try:
    import SCons.Script
except ImportError:
    print "Could not find SCons in '%s'" % scons_dir
    sys.exit(1)

SCons.Script.main()
