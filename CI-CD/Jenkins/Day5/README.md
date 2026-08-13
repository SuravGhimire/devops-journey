# Jenkins Day 5 - Environment Variables and Build Parameters

## Overview

On Day 5 of my Jenkins learning journey, I learned how to make Jenkins Pipelines more dynamic using build parameters and environment variables.

The goal was to use a single Jenkins Pipeline for multiple deployment environments instead of creating separate pipelines.

## Topics Covered

- Jenkins Build Parameters
- Choice Parameters
- Environment Variables
- Custom Environment Variables
- Jenkins Built-in Variables
- Jenkins WORKSPACE
- Pipeline as Code
- Dynamic Pipeline Behavior

## Build Parameter

A choice parameter named `ENVIRONMENT` was created with three options:

- development
- staging
- production

This allows the user to select the deployment environment before starting the build.

The selected parameter is accessed using:

```groovy
${params.ENVIRONMENT}
