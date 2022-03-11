#!/bin/bash

cd ..
cd kubernetes

# DEPLOY DB K8 PODS
cd K8-db
files=$(
    find . -maxdepth 1 -name "*.yaml" -type f -printf "%f," |
awk '{ print substr($0,1,(length($0)-1))}'
)
echo $files
kubectl apply -f $files
cd ..


# DEPLOY MS K8 PODS
cd K8-db
files=$(
    find . -maxdepth 1 -name "*.yaml" -type f -printf "%f," |
awk '{ print substr($0,1,(length($0)-1))}'
)
echo $files
kubectl apply -f $files
cd ..


# DEPLOY MS K8 PODS
cd K8-ms
files=$(
    find . -maxdepth 1 -name "*.yaml" -type f -printf "%f," |
awk '{ print substr($0,1,(length($0)-1))}'
)
echo $files
kubectl apply -f $files
cd ..


# # DEPLOY FE K8 PODS
# cd K8-fe
# files=$(
#     find . -maxdepth 1 -name "*.yaml" -type f -printf "%f," |
# awk '{ print substr($0,1,(length($0)-1))}'
# )
# echo $files
# kubectl apply -f $files
# cd ..


# DEPLOY CI K8 PODS
cd K8-ci
files=$(
    find . -maxdepth 1 -name "*.yaml" -type f -printf "%f," |
awk '{ print substr($0,1,(length($0)-1))}'
)
echo $files
kubectl apply -f $files
cd ..


# # DEPLOY CD K8 PODS
# cd K8-cd
# files=$(
#     find . -maxdepth 1 -name "*.yaml" -type f -printf "%f," |
# awk '{ print substr($0,1,(length($0)-1))}'
# )
# echo $files
# kubectl apply -f $files
# cd ..

cd ..
cd scripts