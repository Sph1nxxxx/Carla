#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ------------------------------------------------------------------------------------------------------------
# Imports (cx_Freeze)

from cx_Freeze import setup, Executable
from os import getenv

# ------------------------------------------------------------------------------------------------------------
# Imports (Custom Stuff)

from carla_host import VERSION

# ------------------------------------------------------------------------------------------------------------

SCRIPT_NAME = getenv("SCRIPT_NAME")

options = {
  "zip_include_packages": ["*"],
  "zip_exclude_packages": ["PyQt5"],
  "replace_paths": [["*","@executable_path/"]],
  "optimize": True,
}

boptions = {
  "iconfile": "./resources/ico/carla.icns"
}

if SCRIPT_NAME in ("Carla", "Carla-Control"):
  boptions["custom_info_plist"] = "./data/macos/%s_Info.plist" % SCRIPT_NAME

setup(name = "Carla",
      version = VERSION,
      description = "Carla Plugin Host",
      options = {"build_exe": options, "bdist_mac": boptions},
      executables = [Executable("./source/frontend/%s.pyw" % SCRIPT_NAME)])

# ------------------------------------------------------------------------------------------------------------
