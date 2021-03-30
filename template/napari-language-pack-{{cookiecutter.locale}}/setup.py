# Copyright (c) 2021, napari
# Distributed under the terms of the BSD 3-Clause License

# Standard library imports
import ast
import os

# Third party imports
from setuptools import find_packages, setup

# Constants
HERE = os.path.abspath(os.path.dirname(__file__))


def get_version(module="napari_language_pack_{{cookiecutter.locale_underscore}}"):
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
    name="napari-language-pack-{{cookiecutter.locale}}",
    version=get_version(),
    url="https://github.com/napari/napari-language-packs",
    description="napari {{ cookiecutter.language }} Language Pack",
    long_description=get_description(),
    long_description_content_type="text/markdown",
    keywords=["napari", "language", "language pack", "localization"],
    author="napari",
    license="BSD-3-Clause",
    platforms="Linux, Mac OS X, Windows",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Framework :: napari",
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
    ],
    entry_points={
        "napari.languagepack": ["{{cookiecutter.locale_underscore}} = napari_language_pack_{{cookiecutter.locale_underscore}}"]
    },
)
