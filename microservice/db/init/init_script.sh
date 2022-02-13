#!/bin/bash
apt update 
apt upgrade -y
apt install python3-pip	-y
pip3 install Faker mysql-connector-python

# add commands to connect to mysql and populate user data