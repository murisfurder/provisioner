#!/bin/bash

# Build Worker
docker build -t cloudnet/worker -f Dockerfile.worker .

docker-compose up

