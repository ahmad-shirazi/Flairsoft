#!/usr/bin/env bash
set -e

echo "current env is dev"
cd src
services=(hospital disease patient userManagement)

for service in ${services[@]}
do
    cd $service
    ls
    echo "Running $service migrations ..."
#    npm install -g knex
    NODE_ENV=DEVELOPMENT knex migrate:latest
    cd ..
done