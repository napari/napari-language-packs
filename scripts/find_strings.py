"""
"""

import os
import sys
import tokenize


def find_strings(path):
    for root, _dirs, files in os.walk(".", topdown = False):
        for filename in files:
            print(os.path.join(root, filename))
            if filename.endswith(".py"):
                with open(filename) as f:
                    for toktype, tokstr, (lineno, _), _, _ in tokenize.generate_tokens(f.readline):
                        if toktype == tokenize.STRING:
                            strrepr = repr(eval(tokstr))
                            print(filename, lineno, strrepr)


if __name__ == "__main__":
    path = sys.argv[1]
    find_strings(path)
