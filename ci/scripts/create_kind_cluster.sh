#!/bin/sh

# INSTALL kubectl
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
kubectl version --client

# INSTALL kind
curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.11.1/kind-linux-amd64
chmod +x ./kind
mv ./kind /root/kind
kind -version

# DEPLOY AND CONFIGURE KIND CLUSTER
kind create cluster --config jenkins-config.yaml
kubectl cluster-info --context kind-kind
kubectl create namespace jenkins
kubectl create serviceaccount jenkins --namespace=jenkins
kubectl describe secret $(kubectl describe serviceaccount jenkins --namespace=jenkins | grep Token | awk '{print $2}') --namespace=jenkins
kubectl create rolebinding jenkins-admin-binding --clusterrole=admin --serviceaccount=jenkins:jenkins --namespace=jenkins