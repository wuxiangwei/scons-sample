# -*- mode: python; -*-

import os
import buildscripts

# import atexit
# import galaxy
# atexit.register(galaxy.print_build_failures)

project_root = os.path.normpath(os.getcwd())
src_dir = os.path.join(project_root, 'src')
build_dir = os.path.join(project_root, 'build')

def make_variant_dir_generator():
    memoized_variant_dir = [False]
    def generate_variant_dir(target, source, env, for_signature):
        if not memoized_variant_dir[0]:
            memoized_variant_dir[0] = env.subst('$BUILD_ROOT/$VARIANT_DIR')
        return memoized_variant_dir[0]
    return generate_variant_dir


env_dict = dict(
    BUILD_ROOT=build_dir,
    BUILD_DIR=make_variant_dir_generator(),
)

# env = Environment(variables=env_vars,  **env_dict)
env = Environment(**env_dict)
del env_dict

# --- lint ---

def do_lint(env, target, source):
    dirs = env.GetBuildPath( source )
    from buildscripts import cpplint_wrapper
    #  cpplint_wrapper.run( ['src'] )
    cpplint_wrapper.do_lint( dirs)


env.Alias('lint', ['src/common', 'src/test'], [do_lint])
env.AlwaysBuild("lint")

env.SConscript(
    dirs=[
        src_dir,
    ],
    duplicate=False,
    exports=[
        'env',
    ],
    variant_dir='$BUILD_DIR',
    install_dir='$BUILD_DIR'
)
