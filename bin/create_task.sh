#!/bin/bash

ENDPOINT="http://192.168.56.132:8080/submit"

curl -H "Content-Type: application/json" \
    -X POST -d '{"role": "ping", "ip": "192.168.33.10", "password": "foobar123", "username": "root"}' \
    $ENDPOINT

curl -H "Content-Type: application/json" \
    -X POST -d '{"role": "ping", "ip": "192.168.33.11", "password": "foobar12", "username": "root"}' \
    $ENDPOINT

curl -H "Content-Type: application/json" \
    -X POST -d '{"role": "docker", "ip": "192.168.33.10", "password": "foobar123", "username": "root"}' \
    $ENDPOINT

curl -H "Content-Type: application/json" \
    -X POST -d '{"role": "docker", "ip": "192.168.33.11", "password": "foobar12", "username": "root"}' \
    $ENDPOINT
