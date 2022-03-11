#!/bin/bash

cd ..
cd ansible
kubectl use-context dev
kubectl create -f ./kubernetes/cluster/aline-secrets.yaml
kubectl create -f ./kubernetes/cluster/aline-configmap.yaml
kubectl create -f ./kubernetes/cluster
