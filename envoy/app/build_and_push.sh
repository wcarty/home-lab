# build_and_push.sh
#!/bin/bash
REGISTRY=wcarty
IMAGE_NAME=webapp
TAG=latest

#echo "Building Docker image..."
#docker build -t $REGISTRY/$IMAGE_NAME:$TAG ./app

#echo "Pushing Docker image to registry..."
#docker push $REGISTRY/$IMAGE_NAME:$TAG

#echo "Done."

echo "Building Docker image and pushing to registry..."
docker buildx create --use

docker buildx build --platform linux/amd64,linux/arm64 \
  -t $REGISTRY/$IMAGE_NAME:$TAG ./app --push

echo "Done."
