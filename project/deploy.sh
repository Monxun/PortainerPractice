#!/bin/sh

cd apps/scripts
source ./deploy_db.sh
sleep 2m
cd scripts
source ./deploy_backend.sh
# source ./deploy_frontend.sh