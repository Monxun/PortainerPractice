#!/bin/sh

apt update
apt install python3-pip	-y
pip3 install -r requirements.txt
# sqlacodegen mysql+pymysql://user:root@localhost/alinedb
python3 producer.py