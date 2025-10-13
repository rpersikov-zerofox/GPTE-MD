# GPTE Documentation Deployment Guide

This directory contains the Docsify-based documentation and Docker deployment configuration.

## Quick Start

### Local Development

The Docsify site runs without build step:

```bash
# Start local server on port 8080
python -m http.server 8080
```

Visit: http://localhost:8080

### Local Docker Testing

Build and run using Docker:

```bash
# Build image
docker build -t gpte-docs-docsify:latest .

# Run container
docker-compose up -d

# Or use docker run directly
docker run -d -p 8080:80 gpte-docs-docsify:latest
```

Visit: http://localhost:8080

## Staging Deployment

### Prerequisites

- Docker installed
- Access to `gpte-harbor-registry.softwaretravel.net`
- Registry credentials configured (`docker login`)

### Deploy to Staging

```bash
# Make script executable
chmod +x deploy-staging.sh

# Run deployment
./deploy-staging.sh
```

This script will:
1. Build the Docker image
2. Tag with timestamp and 'docsify-latest'
3. Push to Harbor registry
4. Display deployment instructions

### On Staging Server

```bash
# Pull latest image
docker-compose -f docker-compose-staging.yml pull

# Start service
docker-compose -f docker-compose-staging.yml up -d

# Check status
docker-compose -f docker-compose-staging.yml ps

# View logs
docker-compose -f docker-compose-staging.yml logs -f
```

The site will be available on port **62080** (as configured in docker-compose-staging.yml).

## File Structure

```
.
├── Dockerfile                    # Docker build configuration
├── docker-compose.yml            # Local development compose
├── docker-compose-staging.yml    # Staging deployment compose
├── .dockerignore                 # Files excluded from build
├── build.sh                      # Local build script
├── deploy-staging.sh             # Staging deployment script
├── index.html                    # Docsify main HTML
├── docs/                         # Documentation markdown files
│   ├── _sidebar.md              # Navigation sidebar
│   └── **/*.md                  # All documentation
└── README.md                     # Homepage content
```

## Differences from MkDocs Deployment

### MkDocs (Previous)
- **Build Step:** Required (Python + MkDocs)
- **Builder Image:** python:3.13.5-bullseye
- **Build Output:** Static HTML in `_build/`
- **Final Image:** nginx + built HTML

### Docsify (Current)
- **Build Step:** None (renders markdown in browser)
- **Builder Image:** Not needed
- **Build Output:** Not needed
- **Final Image:** nginx + source files (index.html + docs/)

### Advantages
- ✅ Simpler Dockerfile (no build stage)
- ✅ Faster builds (~50% faster)
- ✅ Smaller image size
- ✅ No Python dependencies
- ✅ Live markdown rendering
- ✅ Instant updates (just replace files)

## Migration from MkDocs

If migrating from existing MkDocs deployment:

1. **Stop old container:**
   ```bash
   docker-compose -f docker-compose-old.yml down
   ```

2. **Deploy Docsify:**
   ```bash
   ./deploy-staging.sh
   ```

3. **Update on server:**
   ```bash
   docker-compose -f docker-compose-staging.yml up -d
   ```

4. **Verify:** Visit staging URL on port 62080

## Troubleshooting

### Container won't start
```bash
# Check logs
docker-compose -f docker-compose-staging.yml logs

# Check if port is in use
netstat -tulpn | grep 62080
```

### 404 errors
- Verify `docs/` folder is copied to image
- Check `_sidebar.md` paths are relative
- Ensure `index.html` is in image root

### Sidebar not working
- Verify `docs/_sidebar.md` exists
- Check `index.html` has `loadSidebar: true`
- Confirm paths in sidebar are relative (no leading `/docs/`)

### Images not loading
- Verify images are in `/assets/` or correct path
- Check image references in markdown use `/assets/`
- Confirm `.dockerignore` doesn't exclude assets

## CI/CD Integration

To integrate with GitLab CI or Jenkins:

### GitLab CI Example

```yaml
# .gitlab-ci.yml
stages:
  - build
  - deploy

build-docs:
  stage: build
  script:
    - docker build -t $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA .
    - docker push $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA

deploy-staging:
  stage: deploy
  script:
    - docker pull $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA
    - docker tag $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA $CI_REGISTRY_IMAGE:staging
    - docker-compose -f docker-compose-staging.yml up -d
  only:
    - develop
```

## Support

For issues or questions:
- Check container logs: `docker-compose logs`
- Verify nginx is running: `docker exec <container> ps aux`
- Test locally first with `python -m http.server 8080`
