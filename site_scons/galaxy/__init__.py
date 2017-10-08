# -*- mode: python; -*-
# coding:utf-8

def print_build_failures():
    from SCons.Script import GetBuildFailures
    for bf in GetBuildFailures():
        print "[GALAXY] %s failed: %s" % (bf.node, bf.errstr)
