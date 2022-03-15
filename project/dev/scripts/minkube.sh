#!/bin/sh

minikube start
minikube addons enable ingress
kubectl get pod -n kube-system