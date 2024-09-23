# MIT License
#
# Copyright (c) 2024 QIUYIXIANG
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


# Git let Core Code

# Here list all dependent components, In order for compatible for
# further change, and some implemented API for C/C++ Program
import argparse
import datetime
import collections
import configparser
import grp
import pwd
import fnmatch
import hashlib
import os
import zlib
import sys
import re
from math import ceil
from lib import config



def main(argv=sys.argv[1:]) -> None:
    # Initialized and parse the command line argument
    arg_parser = argparse.ArgumentParser(prog=f"Gitlet Version {config.VERSION_NUMBER}",
        description="A lightweight tool for git-like version control system.")




