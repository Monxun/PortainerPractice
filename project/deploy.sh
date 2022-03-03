#!/bin/bash

cd apps/scripts

docker network create -d bridge aline

# DB DEPLOY
source ./deploy_db.sh
cd scripts
source ./deploy_backend.sh
cd scripts
echo "SERVICES INTIALIZING... 2m"
sleep 2m
echo "STEP-4: DEPLOY PRODUCERS"
source ./deploy_ci.sh

# BACKEND DEPLOY
#sleep 1m
#docker build -t ms-underwriter -f ./dockerfiles/backend/Dockerfile.underwriter ./dockerfiles/backend
#docker build -t ms-bank -f ./dockerfiles/backend/Dockerfile.bank ./dockerfiles/backend
#docker build -t ms-transaction -f ./dockerfiles/backend/Dockerfile.transaction ./dockerfiles/backend
#docker build -t ms-gateway -f ./dockerfiles/backend/Dockerfile.gateway ./dockerfiles/backend

#docker run -p 8071:8071 --env-file ./dockerfiles/backend/env/.env.underwriter --name=ms-underwriter --network=aline ms-underwriter
#sleep 1m
#docker run -p 8083:8083 --env-file ./dockerfiles/backend/env/.env.bank --name=ms-bank --network=aline ms-bank 
#sleep 1m
#docker run -p 8073:8073 --env-file ./dockerfiles/backend/env/.env.transaction --name=ms-transaction --network=aline ms-transaction 
#sleep 1m
#docker run -p 8070:8070 --env-file ./dockerfiles/backend/env/.env.user --name=ms-user --network=aline ms-user 
#sleep 1m
#docker run -p 8080:8080 --env-file ./dockerfiles/backend/env/.env.gateway --name=ms-gateway --network=aline ms-gateway 

# FRONTEND DEPLOY
# source ./deploy_frontend.sh