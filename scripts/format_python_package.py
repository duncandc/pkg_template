#!/bin/bash

import os
import argparse


def _replace_pkg_template_with_pkgname(pkg_fname, new_pkgname):
    with open(pkg_fname, 'r') as f:
        new_raw_lines = [raw_line.replace('pkg_template', new_pkgname) for raw_line in f]

    with open(pkg_fname, 'w') as f:
        for line in new_raw_lines:
            f.write(line)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("pkgname", help="Name of the package being created")
    args = parser.parse_args()
    pkgname = args.pkgname
    root_dirname_pkg = os.path.abspath(pkgname)

    #  Search for 'pkg_template' and replace with pkgname in the following files:
    setup_fname = os.path.join(root_dirname_pkg, 'setup.py')
    readme_fname = os.path.join(root_dirname_pkg, 'README.md')
    fnames_to_modify = [setup_fname, readme_fname]
    for fname in fnames_to_modify:
        _replace_pkg_template_with_pkgname(fname, pkgname)
