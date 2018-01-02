#!/bin/sh
# Run me from /scripts/
jupyter-2.7 nbconvert --to markdown Artwork\ Classification.ipynb --config jupyterconverter/jekyll.py
mv ../assets/Artwork-Classification.md ../_posts/2018-1-1-Artwork-Classification.md
