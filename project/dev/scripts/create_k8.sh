#!/bin/bash

cd ..
cd ansible

kubectl create -f ./kubernetes/config/aline-secrets.yaml --namespace=dev
kubectl create -f ./kubernetes/config/aline-configmap.yaml --namespace=dev
# kubectl create -f ./kubernetes/config/aline-ingress.yaml --namespace=dev
kubectl create -f ./kubernetes/config/mysql-pv.yaml --namespace=dev
kubectl create -f ./kubernetes/cluster --namespace=dev

cd ..
cd scripts

# DEPLOY NETSHOOT TOOL CONTAINER
kubectl run tmp-shell --rm -it --image bretfisher/netshoot -- bash

# sleep 1m
# source access-database.sh