#!/bin/bash

cd ..
cd ansible
kubectl delete -f ./kubernetes/cluster
kubectl delete -f ./kubernetes/config

cd ..
cd scripts