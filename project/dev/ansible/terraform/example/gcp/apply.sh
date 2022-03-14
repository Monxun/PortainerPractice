#!/bin/sh

terraform init
terraform apply
gcloud container clusters get-credentials aline-cluster-gke --zone=us-west1
gcloud container clusters get-credentials aline-cluster-gke --zone=us-west1