#!/bin/sh

su
apt update
apt upgrade -y
apt install python3-pip -y
npm install --silent
