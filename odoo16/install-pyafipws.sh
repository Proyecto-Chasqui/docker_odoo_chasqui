#!/bin/bash
pip download https://github.com/reingart/pyafipws/archive/main.zip
python3 -m zipfile -e main.zip  .
cd pyafipws-main
pip install -r requirements.txt --user
python3 setup.py install