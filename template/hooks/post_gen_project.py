# Copyright (c) 2021, napari
# Distributed under the terms of the BSD 3-Clause License

import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))
