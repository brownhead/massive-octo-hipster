#!/usr/bin/env bash

# This will ensure that the script exits if a failure occurs
set -e

# This will echo every line
set -x

apt-get update

apt-get install -y build-essential python3-pip python3-venv python3-dev

pip3 install uwsgi

python3 -m venv /opt/app/venv
/opt/app/venv/bin/pip install -r /opt/app/repo/requirements.txt

# NOTE: This won't affect /opt/app/repo if it was mounted by vagrant
chown -R root:root /opt/app
chmod -R o-w /opt/app
