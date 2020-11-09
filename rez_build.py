import os, subprocess, sys
import zipfile
import urllib.request
import shutil

if __name__ == "__main__":
    src = os.environ["HOUDINI_ROOT"]
    dst = os.environ["REZ_BUILD_INSTALL_PATH"]
    inc_dst = os.environ["REZ_BUILD_INSTALL_PATH"] + "/include"
    lib_dst = os.environ["REZ_BUILD_INSTALL_PATH"] + "/lib"
    bin_dst = os.environ["REZ_BUILD_INSTALL_PATH"] + "/bin"
    
    if 'win' in str(sys.platform):

        # Remove existing build
        if os.path.exists(dst):
            print(" - Removing existing build")
            shutil.rmtree(dst, ignore_errors=True)

        shutil.copytree(src + "/toolkit/include/GL", inc_dst + "/GL")
        
        os.mkdir(lib_dst)

        shutil.copy(src + '/custom/houdini/dsolib/glew.lib', lib_dst + "/glew32.lib")
        shutil.copy(src + '/custom/houdini/dsolib/glew.lib', lib_dst + "/glew.lib")
        
        os.mkdir(bin_dst)

        shutil.copy(src + '/bin/glew.dll', bin_dst + "/glew.dll")
