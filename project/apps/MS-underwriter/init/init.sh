#!/bin/bash
apt update
apt install python3-pip	-y
pip3 install Faker mysql-connector-python
python3 producer.py