#!/bin/sh

minikube start
minikube addons enable ingress

# CREATE NAMESPACE AND SET TO NAMESPACE
cd ..
cd ansible
kubectl create -f ./kubernetes/config/namespace-dev.yaml
kubectl config set-context --current --namespace=dev
cd ..
cd scripts

eval $(minikube docker-env)






