# Standard library imports
import os
import sys

# Constants
HERE = os.path.abspath(os.path.dirname(__file__))
REPO_ROOT = os.path.dirname(os.path.dirname(HERE))
LANG_PACKS_DIR = os.path.join(REPO_ROOT, "language-packs")


def parse_release(current_tag):
    """
    Parse the current tag and provide the locale name from it.

    Example
    -------
    >>> parse_release("es-ES@v0.0.1")
    "REPO_ROOT/language-packs/napari-language-pack-es-ES"
    """
    if current_tag is None:
        raise Exception("CURRENT_TAG not defined!")

    if current_tag.count("-") != 1:
        raise Exception(f"CURRENT_TAG '{current_tag}' not valid!")

    if "@" not in current_tag:
        raise Exception(f"CURRENT_TAG '{current_tag}' not valid!")

    if "dev" in current_tag:
        raise Exception(f"CURRENT_TAG '{current_tag}' should not end with `.devN`!")

    locale, _version = current_tag.split("@")
    folder_path = os.path.join(LANG_PACKS_DIR, f"napari-language-pack-{locale}")
    sys.stdout.write(f'{folder_path}')


if __name__ == "__main__":
    current_tag = os.environ.get("CURRENT_TAG")
    parse_release(current_tag)
