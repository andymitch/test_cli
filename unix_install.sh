#!bin/bash

pip install requirements.txt
sudo python3 setup.py install
shred -u $0
rm -r $PWD
