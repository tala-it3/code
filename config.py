#!/usr/bin/env python


"""
Configuration for the project
"""

import os.path


# Folders and files reference
ASSETS_FOLDER = "assets"
INFO_FOLDER = os.path.join(ASSETS_FOLDER, "info")

# Limit infinite while loops due to halt problem
LOOP_LIMIT = 0xFF

# Input marker
INPUT_MARKER = ">>>"
