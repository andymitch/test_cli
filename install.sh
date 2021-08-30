#!bin/bash

pip install requirements.txt
sudo python3 setup.py develop
shred -u $0
rm -r $PWD
