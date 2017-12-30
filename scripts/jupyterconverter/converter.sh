#!/bin/sh
# Run me from /scripts/
jupyter-2.7 nbconvert --to markdown hessian_mnist.ipynb --config jupyterconverter/jekyll.py
mv ../assets/hessian_mnist.md ../_posts/2017-12-28-hessian-mnist.md
