import shutil, os
import sys

print ( "------------------ GENERATING CMAKE ------------------" )

userDirName = "qub3d"

if len(sys.argv) > 1:
	userDirName = sys.argv[1]

script_dir = str( os.path.dirname( os.path.realpath( __file__ ) ) )
root_dir = script_dir + "/../" + userDirName + "/"
print root_dir

cmake_dir = script_dir + "/resources/cmake/"

shutil.copyfile ( cmake_dir + "root.cmake", root_dir + "CMakeLists.txt" )
