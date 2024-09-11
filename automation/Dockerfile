# Use the official PostgreSQL image from the Docker Hub
FROM postgres:latest

# Define build-time arguments
ARG POSTGRES_DB
ARG POSTGRES_USER
ARG POSTGRES_PASSWORD

# Set environment variables from build-time arguments
ENV POSTGRES_DB=${POSTGRES_DB}
ENV POSTGRES_USER=${POSTGRES_USER}
ENV POSTGRES_PASSWORD=${POSTGRES_PASSWORD}

# Copy the SQL file into the container
COPY create-data.sql /docker-entrypoint-initdb.d/

# Expose the default PostgreSQL port
EXPOSE 5432