#!/bin/bash

cd ..
cd ..
cd apps

# BUILD IMAGES

docker-compose -f docker-compose.db.yml build
docker-compose -f docker-compose.ms.yml build
# docker-compose -f docker-compose.fe.yml build
docker-compose -f docker-compose.ci.yml build
# docker-compose -f docker-compose.cd.yml build

# PUSH IMAGES

#//////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////
# BACKEND

docker tag ms-bank:0.1 registry.dev.svc.cluster.local:5001/ms-bank:0.1
docker push registry.dev.svc.cluster.local:5001/ms-bank:0.1

docker tag ms-transaction:0.1 registry.dev.svc.cluster.local:5001/ms-transaction:0.1
docker push registry.dev.svc.cluster.local:5001/ms-transaction:0.1


docker tag ms-underwriter:0.1 registry.dev.svc.cluster.local:5001/ms-underwriter:0.1
docker push registry.dev.svc.cluster.local:5001/ms-underwriter:0.1


docker tag ms-user:0.1 registry.dev.svc.cluster.local:5001/ms-user:0.1
docker push registry.dev.svc.cluster.local:5001/ms-user:0.1


docker tag ms-gateway:0.1 registry.dev.svc.cluster.local:5001/ms-gateway:0.1
docker push registry.dev.svc.cluster.local:5001/ms-gateway:0.1


#//////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////
# FRONTEND

# docker tag fe-admin:0.1 localhost:5001/fe-admin:0.1
# docker push localhost:5001/fe-admin:0.1

# docker tag fe-dashboard:0.1 localhost:5001/fe-dashboard:0.1
# docker push localhost:5001/fe-dashboard:0.1


# docker tag fe-landing:0.1 localhost:5001/fe-landing:0.1
# docker push localhost:5001/fe-landing:0.1

#//////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////
# CI

docker tag ci-producer:0.1 registry.dev.svc.cluster.local:5001/ci-producer:0.1
docker push registry.dev.svc.cluster.local:5001/ci-producer:0.1

