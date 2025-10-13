#!/bin/bash
# Deploy Docsify documentation to staging

set -e

REGISTRY="gpte-harbor-registry.softwaretravel.net/gpte1"
IMAGE_NAME="gpte-docs-staging"
TAG="docsify-$(date +%Y%m%d-%H%M%S)"

echo "Building Docsify documentation..."
docker build -t ${IMAGE_NAME}:${TAG} .

echo "Tagging image for registry..."
docker tag ${IMAGE_NAME}:${TAG} ${REGISTRY}/${IMAGE_NAME}:${TAG}
docker tag ${IMAGE_NAME}:${TAG} ${REGISTRY}/${IMAGE_NAME}:docsify-latest

echo "Pushing to registry..."
docker push ${REGISTRY}/${IMAGE_NAME}:${TAG}
docker push ${REGISTRY}/${IMAGE_NAME}:docsify-latest

echo ""
echo "Deployment complete!"
echo "Image: ${REGISTRY}/${IMAGE_NAME}:${TAG}"
echo "Latest: ${REGISTRY}/${IMAGE_NAME}:docsify-latest"
echo ""
echo "To deploy on staging server:"
echo "  docker-compose -f docker-compose-staging.yml pull"
echo "  docker-compose -f docker-compose-staging.yml up -d"
