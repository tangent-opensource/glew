import os, subprocess, sys
import zipfile
import urllib.request
import shutil

# TODO: We should build glew properly, but ben skinner didn't have the time
# I'm terribly sorry...

if __name__ == "__main__":
    src = os.environ["REZ_BUILD_SOURCE_PATH"]
    dst = os.environ["REZ_BUILD_INSTALL_PATH"] + "/build"

    build_dir = src + "/_rez_build"
    
    if 'win' in str(sys.platform):
        GLEW_URL = "https://downloads.sourceforge.net/project/glew/glew/2.0.0/glew-2.0.0-win32.zip"

        print('Beginning file download with urllib2...')

        zip_path = build_dir + '/glew_2.0.0.zip'
        glew_dir = build_dir + '/glew_expanded'

        urllib.request.urlretrieve(GLEW_URL, zip_path)

        with zipfile.ZipFile(zip_path,"r") as zip_ref:
            zip_ref.extractall(glew_dir)
       
        glew_dir += "/glew-2.0.0"
        
        # Remove existing build
        if os.path.exists(dst):
            print(" - Removing existing build")
            shutil.rmtree(dst, ignore_errors=True)

        dirs = [
            #"bin",
            #"lib",
            "include",
        ]

        for d in dirs:
            try:
                shutil.copytree(glew_dir + "/" + d, dst + "/" + d, ignore=shutil.ignore_patterns('_rez_build', '.git'))
                print(" - Copying: {0} : {1}".format(glew_dir + "/" + d, dst + "/" + d))
            except Exception as e:
                print(" - " + str(e))
                pass

        os.mkdir(dst + "/bin")
        os.mkdir(dst + "/lib")
        shutil.copy(glew_dir + '/bin/Release/x64/glew32.dll', dst + "/bin/glew32.dll")
        shutil.copy(glew_dir + '/lib/Release/x64/glew32.lib', dst + "/lib/glew32.lib")
        # This is needed for cycles...
        shutil.copy(glew_dir + '/lib/Release/x64/glew32.lib', dst + "/lib/glew.lib")



    else:
        GLEW_URL = "https://downloads.sourceforge.net/project/glew/glew/2.0.0/glew-2.0.0.tgz"

        subprocess.run([
            'make',
        ])