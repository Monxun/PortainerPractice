#!/bin/sh

apt update
apt install python3-pip	-y
pip3 install -r project/db/init/requirements.txt
# sqlacodegen mysql+pymysql://user:root@localhost/alinedb
cd project
cd db
cd init
python3 producer.py