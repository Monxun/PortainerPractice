#!/bin/bash

cd ..
cd ansible
kubectl delete -f ./kubernetes/cluster
kubectl delete -f ./kubernetes/config/aline-secrets.yaml --namespace=dev
kubectl delete -f ./kubernetes/config/aline-configmap.yaml --namespace=dev
kubectl delete -f ./kubernetes/config/mysql-pv.yaml --namespace=dev
kubectl delete -f ./kubernetes/config/aline-ingress.yaml --namespace=dev


cd ..
cd scripts