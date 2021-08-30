#!bin/bash

function cleanup {
    shred -u $0
    cd ..
    rm -fr test_cli
}

pip install -r requirements.txt
python3 test_cli/setup.py install

trap cleanup EXIT

echo "removed installer"