#!/bin/bash

cd ..
cd kubernetes

################################################
# BUILD DB K8 FILES

cd K8-db
# kompose -f docker-compose.db.yml convert
docker-compose -f docker-compose.db.yml build

kubectl create deployment db-aline --image=mysql --dry-run -o=yaml > db-aline-deployment.yaml
kubectl create service clusterip db-aline --tcp=3306:3306 --dry-run -o=yaml >> db-aline-service.yaml

kubectl create deployment db-adminer --image=adminer --dry-run -o=yaml > db-adminer-deployment.yaml
kubectl create service clusterip db-adminer --tcp=8084:8080 --dry-run -o=yaml >> db-adminer-service.yaml
cd ..

################################################
# BUILD MS K8 FILES

cd K8-ms
# kompose -f docker-compose.ms.yml convert
docker-compose -f docker-compose.ms.yml build

kubectl create deployment ms-gateway --image=ms-gateway --dry-run -o=yaml > ms-gateway-deployment.yaml
kubectl create service clusterip ms-gateway --tcp=8080:8080 --dry-run -o=yaml >> ms-gateway-service.yaml

kubectl create deployment ms-bank --image=ms-bank --dry-run -o=yaml > ms-bank-deployment.yaml
kubectl create service clusterip ms-bank --tcp=8083:8083 --dry-run -o=yaml >> ms-bank-service.yaml

kubectl create deployment ms-transaction --image=ms-transaction --dry-run -o=yaml > ms-transaction-deployment.yaml
kubectl create service clusterip ms-transaction --tcp=8073:8073 --dry-run -o=yaml >> ms-transaction-service.yaml

kubectl create deployment ms-underwriter --image=ms-underwriter --dry-run -o=yaml > ms-underwriter-deployment.yaml
kubectl create service clusterip ms-underwriter --tcp=8071:8071 --dry-run -o=yaml >> ms-underwriter-service.yaml

kubectl create deployment ms-user --image=ms-user --dry-run -o=yaml > ms-user-deployment.yaml
kubectl create service clusterip ms-user --tcp=8070:8070 --dry-run -o=yaml >> ms-user-service.yaml

cd ..

################################################
# # BUILD FE K8 FILES

cd K8-fe
# kompose -f docker-compose.fe.yml convert
# docker-compose -f docker-compose.fe.yml build
cd ..

################################################
# BUILD CI K8 FILES

cd K8-ci
# kompose -f docker-compose.ci.yml convert
docker-compose -f docker-compose.ci.yml build

kubectl create deployment ci-producer --image=ci-producer --dry-run -o=yaml > ci-producer-deployment.yaml
kubectl create service clusterip ci-producer --tcp=5050:5050 --dry-run -o=yaml >> ci-producer-service.yaml

cd ..

################################################
# # BUILD CD K8 FILES

cd K8-cd
# kompose -f docker-compose.cd.yml convert
# docker-compose -f docker-compose.cd.yml build
cd ..

################################################
cd ..
cd scripts
