#!/bin/bash
# Build script for Docsify documentation Docker image

set -e

echo "Building Docsify documentation Docker image..."

# Build the image
docker build -t gpte-docs-docsify:latest .

echo "Build complete!"
echo "Image: gpte-docs-docsify:latest"
