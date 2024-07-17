#!/bin/bash

# ./run_docker_composes.sh

cd bdd_traducteur
docker compose up -d
sleep 3 

cd ../api_traducteur
docker compose up -d
sleep 6 

cd ../web_traducteur
docker compose up -d
sleep 3