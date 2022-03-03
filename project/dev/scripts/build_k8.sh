#!/bin/bash

cd ..
cd kubernetes

# BUILD DB K8 FILES
cd K8-db
kompose -f docker-compose.db.yml convert
cd ..

# BUILD MS K8 FILES
cd K8-ms
kompose -f docker-compose.ms.yml convert
cd ..

# # BUILD FE K8 FILES
cd K8-fe
# kompose -f docker-compose.fe.yml convert
cd ..

# BUILD CI K8 FILES
cd K8-ci
kompose -f docker-compose.ci.yml convert
cd ..

# # BUILD CD K8 FILES
cd K8-cd
# kompose -f docker-compose.cd.yml convert
cd ..
