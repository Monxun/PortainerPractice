#!/bin/sh

apt update
apt install python3-pip	-y
pip3 install -r requirements.txt
sqlacodegen --generator tables mysql+pymysql://$MYSQL_USER:$MYSQL_PASSWORD@localhost/$MYSQL_DATABASE
