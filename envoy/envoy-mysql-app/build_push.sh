#!/bin/bash

# Set Docker Hub username
DOCKER_USER="wcarty"

# Image names
ENVOY_IMAGE="$DOCKER_USER/envoy-proxy"
APP_IMAGE="$DOCKER_USER/python-app"
MYSQL_IMAGE="$DOCKER_USER/mysql-db"

# Ensure script exits on failure
set -e

echo "Logging in to Docker Hub..."
docker login

echo "Building and pushing MySQL image..."
docker buildx build --platform linux/amd64 -t $MYSQL_IMAGE:latest -f mysql/Dockerfile mysql/ --push

echo "Building and pushing Envoy Proxy image..."
#docker buildx build --platform linux/amd64,linux/arm64 -t $ENVOY_IMAGE:latest -f envoy/Dockerfile envoy/ --push

echo "Building and pushing Python App image..."
docker buildx build --platform linux/amd64 -t $APP_IMAGE:latest -f app/Dockerfile app/ --push

echo "All images built and pushed successfully!"
