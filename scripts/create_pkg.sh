#!/bin/bash

git clone https://github.com/aphearin/pkg_template.git

cp pkg_template/scripts/format_python_package.py ./
python format_python_package.py $1 $2

rm format_python_package.py
rm -rf pkg_template
