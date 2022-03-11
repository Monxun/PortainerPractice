#!/bin/bash

cd ..
cd ansible
kubectl delete -f ./kubernetes/cluster

cd ..
cd scripts