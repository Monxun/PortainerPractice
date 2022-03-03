#!/bin/sh

# CREATE SCRIPT TO SETUP CICD PIPELINE AND STAGING SERVER ON SEPARATE NETWORKS OR SERVERS

apt update
apt install python3-pip	-y
pip3 install -r project/db/init/requirements.txt
# sqlacodegen mysql+pymysql://user:root@localhost/alinedb
python3 /project/db/init/producer.py