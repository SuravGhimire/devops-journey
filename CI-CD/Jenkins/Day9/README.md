# Jenkins Day 9 — Jenkins + Docker Integration

## Overview

In Day 9, I integrated Jenkins with Docker and created a CI pipeline that builds, runs, tests, and cleans up a Docker container.

## Topics Covered

- Jenkins Docker integration
- Docker permissions for Jenkins
- Docker image building
- Docker container execution
- Container testing
- Container cleanup

## Practical Implementation

Jenkins builds a Docker image using the Day 9 Dockerfile.

The image runs an Nginx application that displays:

`Hello from Jenkins + Docker!`

The pipeline then starts the container on port `8090` and tests it using `curl`.

## Pipeline Flow

GitHub → Jenkins → Build Docker Image → Run Container → Test → Cleanup

## Result

The Jenkins pipeline successfully:

1. Built the Docker image.
2. Started the Docker container.
3. Tested the application.
4. Removed the container after testing.
5. Completed successfully.

## Key Learning

Jenkins can automate Docker-based CI workflows by building images, running containers, testing applications, and cleaning up resources automatically.
