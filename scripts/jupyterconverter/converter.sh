#!/bin/sh
# Run me from /scripts/
# converter.sh BASENAME YYYY-MM-DD
jupyter nbconvert --to markdown $1.ipynb --config jupyterconverter/jekyll.py
mv ../assets/$1.md ../_posts/$2-$1.md
