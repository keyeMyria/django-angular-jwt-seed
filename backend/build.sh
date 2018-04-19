#!/usr/bin/env bash
apt install -y python3-venv
python3 -m venv ../venv3.6/
. ../venv3.6/bin/activate
pip install -r requirements.txt --verbose

