#!/bin/sh

cd scripts
source ./deploy_db.sh
sleep 1m
source ./deploy_backend.sh
# source ./deploy_frontend.sh