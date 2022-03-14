#!/bin/sh

cd project
source build.sh
cd ..
cd ..
cd dev
cd scripts
source kind_registry.sh
source build_images.sh
source create_k8.sh