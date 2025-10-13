# Multi-stage build for Docsify documentation
# Stage 1: No build needed - Docsify is runtime only
FROM nginx:1.29.0-bookworm

# Copy Docsify files to nginx html directory
COPY index.html /usr/share/nginx/html/
COPY docs/ /usr/share/nginx/html/docs/
COPY README.md /usr/share/nginx/html/

# Expose port 80
EXPOSE 80

# Nginx runs by default, no custom command needed
