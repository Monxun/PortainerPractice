#!/bin/sh

# INSTALL PYTHON AND KOMPOSE

apt update
apt upgrade -y
apt install python3-pip	-y

wget https://github.com/kubernetes/kompose/releases/download/v1.26.1/kompose_1.26.1_amd64.deb
sudo apt install ./kompose_1.26.1_amd64.deb -y

# TODO: CREATE SCRIPT TO SETUP CICD PIPELINE AND STAGING SERVER ON SEPARATE NETWORKS OR SERVERS
