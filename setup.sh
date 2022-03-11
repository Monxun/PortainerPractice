#!/bin/sh

# INSTALL PYTHON AND KOMPOSE

apt update
apt install python3-pip	-y
apt install conntrack
apt install net-tools

wget https://github.com/kubernetes/kompose/releases/download/v1.26.1/kompose_1.26.1_amd64.deb # Replace 1.26.1 with latest tag
sudo apt install ./kompose_1.26.1_amd64.deb -y

# RUN DOCKER BENCH TO CHECK INSTALLATION ALSO RUN AFTER DEPLOYMENT TO VERIFY HEALTH

git clone https://github.com/docker/docker-bench-security.git
cd docker-bench-security
sudo sh docker-bench-security.sh

# INSTALL ZSH
apt-get install zsh -y
