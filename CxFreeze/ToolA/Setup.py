import sys
import os
from cx_Freeze import setup, Executable

#
# Get UTILITY_NAME and Relative Directory, if any.
#

Path = sys.argv [0]
Dir = os.path.dirname (Path)
RelDir = os.path.dirname (Dir)[len (os.getcwd ()) + 1:]
UTILITY_NAME = os.path.basename (Dir)
if RelDir:
  RelDir += "\\"

#
# Build EXE file.
#

Exe1 = Executable (
        script=r"%s%s\%s.py" % (RelDir, UTILITY_NAME, UTILITY_NAME),
        base=None,
        appendScriptToExe = True,
        appendScriptToLibrary = False,
        )

includes = []
excludes = []
packages = []
path = sys.path + [".", "..", RelDir]

setup (
    name = UTILITY_NAME,
    version = "0.1",
    description = UTILITY_NAME,
    executables = [Exe1],
    options = {
        "build_exe": {
            "includes": includes,
            "excludes": excludes,
            "packages": packages,
            "path": path,
            "create_shared_zip": False, # don't generate Library.zip
            "append_script_to_exe": True, # don't generate UTILITY_NAME.zip file.
            }
        }
    )

