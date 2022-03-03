#!/bin/bash

cd ..
cd kubernetes

# DEPLOY DB K8 PODS
cd K8-db
kubectl apply -f *.yaml
cd ..


# DEPLOY MS K8 PODS
cd K8-ms
kubectl apply -f *.yaml
cd ..


# # DEPLOY FE K8 PODS
# cd K8-fe
# kubectl apply -f *.yaml
# cd ..


# DEPLOY CI K8 PODS
cd K8-ci
kubectl apply -f *.yaml
cd ..


# # DEPLOY CD K8 PODS
# cd K8-cd
# kubectl apply -f *.yaml
# cd ..

cd ..
cd scripts