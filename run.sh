#!/bin/bash

# BUILDS AND DEPLOYS ALINE SPRING-BOOT PROJECT

cd project

echo "STEP-1: DESTROY IMAGES AND OLD NETWORKS"
source destroy.sh

echo "STEP-2: BUILD JAR FILES"
source build.sh
cd ..

echo "STEP-3: DEPLOY DB + MS"
source deploy.sh
cd ..
