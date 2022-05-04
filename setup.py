from ctypes.util import find_library
import cx_Freeze
import sys


base = None
if sys.platform.startswith("win"):
    # Hide console on Windows
    base = "Win32GUI"


bin_includes = []

def bundle_libs(*libs):
    for lib in libs:
        if name := find_library(lib):
            bin_includes.append(name)

if sys.platform.startswith("linux"):
    bundle_libs("ffi")

icon = "resources/icons/icon"
if sys.platform.startswith("win"):
    icon += ".ico"
else:
    icon += ".png"

cx_Freeze.setup(
    name="F95Checker",
    description="An update checker tool for (NSFW) games on the F95Zone platform",
    executables=[
        cx_Freeze.Executable(
            script="main.py",
            base=base,
            target_name="F95Checker",
            icon=icon
        )
    ],
    options={
        "build_exe": {
            "build_exe": "dist",
            "optimize": 1,
            "packages": [
                "OpenGL",
            ],
            "bin_includes": bin_includes,
            "include_files": [
                "resources",
                "LICENSE"
            ],
            "silent_level": 1,
            "include_msvcr": True
        }
    }
)