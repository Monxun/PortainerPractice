#!/bin/sh

# UPDATE/INSTALL PACKAGES
apt update
apt upgrade -y
apt install python3-pip	-y
apt install conntrack
apt install snap -y
apt install npm -y
apt install maven -y
npm -g install create-react-app

# INSTALL ZSH
apt-get install zsh -y
