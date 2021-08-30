#!bin/bash

pip install - requirements.txt
python3 test_cli/setup.py install
shred -u $0
rm -r $PWD
