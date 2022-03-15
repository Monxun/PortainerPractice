#!/bin/sh

minikube start --cpus 4 --memory 4096 --insecure-registry registry.dev.svc.cluster.local:5001
minikube addons enable ingress

# CREATE NAMESPACE AND SET TO NAMESPACE
cd ..
cd ansible
kubectl create -f ./kubernetes/config/namespace-dev.yaml
kubectl config set-context --current --namespace=dev
cd ..
cd scripts







