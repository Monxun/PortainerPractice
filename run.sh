#!/bin/bash

# BUILDS AND DEPLOYS ALINE SPRING-BOOT PROJECT

cd project
echo "STEP-1: DESTROY IMAGES AND OLD NETWORKS"
source destroy.sh
echo "STEP-2: BUILD JAR FILES"
source build.sh
echo "STEP-3: DEPLOY DB + MS"
source deploy.sh
echo "(SERVICES INITIALIZING... 2 MINUTES)"
sleep 2 min
echo "STEP-4: DEPLOY PRODUCERS"
source cicd.sh
echo "STEP-5: CREATE KUBERNETES FILES FROM COMPOSE FILES"
source k8.sh