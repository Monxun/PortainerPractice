#!/bin/sh

# INSTALL PYTHON AND KOMPOSE

apt update
apt install python3-pip	-y
apt install conntrack
apt install net-tools

wget https://github.com/kubernetes/kompose/releases/download/v1.26.1/kompose_1.26.1_amd64.deb # Replace 1.26.1 with latest tag
sudo apt install ./kompose_1.26.1_amd64.deb -y

curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube

# TODO: CREATE SCRIPT TO SETUP CICD PIPELINE AND STAGING SERVER ON SEPARATE NETWORKS OR SERVERS
