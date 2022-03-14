#!/bin/sh

cd ..

cd FE-admin
npm run build
cd ..

cd FE-dashboard
npm run build
cd ..

cd FE-admin
npm run build
cd ..

cd scripts