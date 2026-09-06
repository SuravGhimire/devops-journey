# Jenkins Day 6 — Conditional Stages and Post Actions

## Overview

In Day 6, I learned how to control Jenkins Pipeline execution using conditional stages and post-build actions.

## Topics Covered

- Jenkins `when` directive
- Conditional stage execution
- Build parameters
- Environment-based deployment
- Jenkins `post` section
- `success`, `failure`, and `always` conditions

## Practical Implementation

The pipeline accepts an `ENVIRONMENT` parameter:

- development
- staging
- production

Based on the selected environment, Jenkins executes only the corresponding deployment stage.

## Pipeline Flow

Build → Test → Conditional Deployment → Post Actions

## Key Learning

This approach allows a single Jenkins Pipeline to handle different deployment environments while keeping the CI/CD workflow organized and reusable.
