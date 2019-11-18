#!/bin/bash

import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("pkgname", help="Name of the package being created")
args = parser.parse_args()
pkgname = args.pkgname
root_dirname_pkg = os.path.abspath(pkgname)


#  Modify setup.py
setup_fname = os.path.join(root_dirname_pkg, 'setup.py')
all_raw_lines = []
with open(setup_fname, 'r') as f:
    new_raw_lines = [raw_line.replace('pkg_template', pkgname) for raw_line in f]

with open(setup_fname, 'w') as f:
    for line in new_raw_lines:
        f.write(line)
