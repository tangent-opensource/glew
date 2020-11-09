name = 'glew'

version = '1.1.0-houdini-18.0.532-ta.1.0.0'

authors = [
    'benjamin.skinner',
]

private_build_requires = [
    'python',
    'houdini-18.0.532',
]

variants = [
    ['platform-windows', 'arch-x64', 'os-windows-10'],
]

build_command = 'python {root}/rez_build.py'

def commands():

    # Split and store version and package version
    split_versions = str(version).split('-')
    env.GLEW_VERSION.set(split_versions[0])
    env.GLEW_PACKAGE_VERSION.set(split_versions[1])

    env.GLEW_ROOT.set( "{root}" )
    env.GLEW_ROOT_DIR.set( "{root}" )
    env.GLEW_LIB_DIR.set( "{root}/lib" )
    env.GLEW_INCLUDE_DIR.set( "{root}/include" )

    env.PATH.append( "{root}/bin" )