#!/bin/bash

cd ..
cd ansible

kubectl create -f ./kubernetes/config/aline-secrets.yaml --namespace=dev
kubectl create -f ./kubernetes/config/aline-configmap.yaml --namespace=dev
kubectl create -f ./kubernetes/config/mysql-pv.yaml --namespace=dev
kubectl create -f ./kubernetes/config/aline-ingress.yaml --namespace=dev
kubectl create -f ./kubernetes/cluster --namespace=dev --image-pull-policy=Never

cd ..
cd scripts

# sleep 1m
# source access-database.sh