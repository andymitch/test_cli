#!bin/bash

pip install -r requirements.txt
python3 test_cli/setup.py install
shred -u $0
rm -fr *
echo "removed installer"