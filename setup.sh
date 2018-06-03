#!/bin/bash
mkdir setup
cd setup
git clone https://github.com/zeth/inputs.git
cd inputs
python setup.py install
cd ..
cd ..
rm -rf setup
