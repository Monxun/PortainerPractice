#!/bin/bash

cd ..
cd ..

# BUILD DB K8 FILES
kompose --file ./apps/docker-compose.db.yml convert
find . -maxdepth 1 -name '*.yml' -exec mv {} ./dev/kubernetes/K8-db/ \;

# BUILD MS K8 FILES
kompose --file ./apps/docker-compose.ms.yml convert
find . -maxdepth 1 -name '*.yml' -exec mv {} ./dev/kubernetes/K8-db/ \;

# # BUILD FE K8 FILES
# kompose --file ./apps/docker-compose.fe.yml convert
# find . -name '*.yml' -exec mv {} ./dev/kubernetes/K8-fe/ \;

# BUILD CI K8 FILES
kompose --file ./apps/docker-compose.ci.yml convert
find . -maxdepth 1 -name '*.yml' -exec mv {} ./dev/kubernetes/K8-db/ \;

# # BUILD CD K8 FILES
# kompose --file ./apps/docker-compose.ci.yml convert
# find . -name '*.yml' -exec mv {} ./dev/kubernetes/K8-cd/ \;