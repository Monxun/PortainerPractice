#!/bin/bash

cd dev/kubernetes

# DEPLOY DB K8 PODS
cd K8-db
files=( /K8-db/*.yml )
remove=docker-compose.db.yml
kubectl apply -f "${files[@]/$remove}"
cd ..

# DEPLOY MS K8 PODS
cd K8-ms
files=( /K8-ms/*.yml )
remove=docker-compose.ms.yml
kubectl apply -f "${files[@]/$remove}"
cd ..

# # DEPLOY FE K8 PODS
# cd K8-fe
# files=( /K8-fe/*.yml )
# remove=docker-compose.fe.yml
# kubectl apply -f "${files[@]/$remove}"
# cd ..

# DEPLOY CI K8 PODS
cd K8-ci
files=( /K8-ci/*.yml )
remove=docker-compose.ci.yml
kubectl apply -f "${files[@]/$remove}"
cd ..

# # DEPLOY CD K8 PODS
# cd K8-cd
# files=( /K8-cd/*.yml )
# remove=docker-compose.cd.yml
# kubectl apply -f "${files[@]/$remove}"
# cd ..

cd ..
cd scripts