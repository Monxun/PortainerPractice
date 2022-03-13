#!/bin/bash

export GCE_EMAIL=929311697798-compute@developer.gserviceaccount.com 
export GCE_PROJECT=aline-financial
export GCE_CREDENTIALS_FILE_PATH=key.json
export GCP_PROJECT=aline-financial
export GCP_AUTH_KIND=serviceaccount
export GCP_SERVICE_ACCOUNT_FILE=key.json
export GCP_SCOPES=https://www.googleapis.com/auth/compute
export GCP_REGION=us-west1-a
export GCP_ZONE=us-west1-a

$ ssh-keygen -o -a 100 -t ed25519 -f ~/.ssh/k8_node -C "first.last@domain.com"