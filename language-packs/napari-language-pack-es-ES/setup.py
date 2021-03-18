# Copyright (c) 2021, napari
# Distributed under the terms of the BSD 3-Clause License

# Standard library imports
import ast
import os

# Third party imports
from setuptools import find_packages, setup

# Constants
HERE = os.path.abspath(os.path.dirname(__file__))


def get_version(module="napari_language_pack_es_ES"):
    """Get version."""
    with open(os.path.join(HERE, module, "__init__.py"), "r") as f:
        data = f.read()

    lines = data.split("\n")
    for line in lines:
        if line.startswith("__version__"):
            version = ast.literal_eval(line.split("=")[-1].strip())
            break

    return version


def get_description():
    """Get long description."""
    with open(os.path.join(HERE, "README.md"), "r") as f:
        data = f.read()

    return data


setup(
    name="napari-language-pack-es-ES",
    version=get_version(),
    description="Napari Spanish (Spain) Language Pack",
    long_description=get_description(),
    long_description_content_type="text/markdown",
    keywords=["napari", "language", "language pack", "localization"],
    url="https://github.com/napari/napari-language-packs",
    author="napari",
    license="BSD-3-Clause",
    platforms="Linux, Mac OS X, Windows",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        "napari.languagepack": ["es_ES = napari_language_pack_es_ES"]
    },
)
