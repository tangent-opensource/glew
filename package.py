name = 'glew'

version = '2.0.0-ta.1.1.0'

authors = [
    'benjamin.skinner',
]

private_build_requires = [
    'python-3',
]

variants = [
    ['platform-windows', 'arch-x64', 'os-windows-10'],
]

# Need because rez_build.py still calls compilers
# @early()
# def private_build_requires():
#     import sys
#     if 'win' in str(sys.platform):
#         return ['visual_studio']
#     else:
#         return ['gcc-7']

build_command = 'python {root}/rez_build.py'

def commands():

    # Split and store version and package version
    split_versions = str(version).split('-')
    env.GLEW_VERSION.set(split_versions[0])
    env.GLEW_PACKAGE_VERSION.set(split_versions[1])

    env.GLEW_ROOT.set( "{root}/build" )
    env.GLEW_ROOT_DIR.set( "{root}/build" )
    env.GLEW_LIB_DIR.set( "{root}/lib" )
    env.GLEW_INCLUDE_DIR.set( "{root}/include" )

    env.PATH.append( "{root}/build/bin" )