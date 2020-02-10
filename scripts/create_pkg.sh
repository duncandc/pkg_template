#!/bin/bash

if [ "$1" == "" ]; then
    echo "Must supply an argument for the root directory of the new package"
    exit 125
else
    mkdir $1
fi

git clone https://github.com/aphearin/pkg_template.git

cp pkg_template/scripts/format_python_package.py ./
python format_python_package.py $1

rm format_python_package.py
rm -rf pkg_template
