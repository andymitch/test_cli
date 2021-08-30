#!bin/bash

pip install -r test_cli/requirements.txt
python3 test_cli/setup.py install
shred -u $0
rm -fr test_cli
echo "removed installer"