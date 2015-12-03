#!/bin/bash

# Build Docker Containers
docker build -t cloudnet/prov-worker -f Dockerfile.worker .
docker build -t cloudnet/prov-api -f Dockerfile.api .

# Fire up Docker Compose
docker-compose up
