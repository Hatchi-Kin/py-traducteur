#!/bin/bash

# ./run_docker_compose_down.sh

cd web_traducteur
docker compose down
sleep 3

cd ../api_traducteur
docker compose down
sleep 4

cd ../bdd_traducteur
docker compose down