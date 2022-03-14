#!/bin/sh

cd ..

cd FE-admin
sudo npm install
sudo npm run build
cd ..

cd FE-dashboard
sudo npm install
sudo npm run build
cd ..

cd FE-admin
sudo npm install
sudo npm run build
cd ..

cd scripts