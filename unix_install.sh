#!bin/bash

pip install requirements.txt
python3 setup.py install
shred -u $0
rm -r $PWD
