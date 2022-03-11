#!/bin/bash

cd ..
cd kubernetes

# DESTROY DB K8 PODS
cd K8-db
files=$(
    find . -maxdepth 1 -name "*.yaml" -type f -printf "%f," |
awk '{ print substr($0,1,(length($0)-1))}'
)
echo $files
kubectl delete -f $files
cd ..


# DESTROY MS K8 PODS
cd K8-db
files=$(
    find . -maxdepth 1 -name "*.yaml" -type f -printf "%f," |
awk '{ print substr($0,1,(length($0)-1))}'
)
echo $files
kubectl delete -f $files
cd ..


# DESTROY MS K8 PODS
cd K8-ms
files=$(
    find . -maxdepth 1 -name "*.yaml" -type f -printf "%f," |
awk '{ print substr($0,1,(length($0)-1))}'
)
echo $files
kubectl delete -f $files
cd ..


# # DESTROY FE K8 PODS
# cd K8-fe
# files=$(
#     find . -maxdepth 1 -name "*.yaml" -type f -printf "%f," |
# awk '{ print substr($0,1,(length($0)-1))}'
# )
# echo $files
# kubectl delete -f $files
# cd ..


# DESTROY CI K8 PODS
cd K8-ci
files=$(
    find . -maxdepth 1 -name "*.yaml" -type f -printf "%f," |
awk '{ print substr($0,1,(length($0)-1))}'
)
echo $files
kubectl delete -f $files
cd ..


# # DESTROY CD K8 PODS
# cd K8-cd
# files=$(
#     find . -maxdepth 1 -name "*.yaml" -type f -printf "%f," |
# awk '{ print substr($0,1,(length($0)-1))}'
# )
# echo $files
# kubectl delete -f $files
# cd ..

cd ..
cd scripts