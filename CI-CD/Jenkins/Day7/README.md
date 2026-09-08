# Jenkins Day 7 — Build Artifacts

## Overview

In Day 7, I learned how Jenkins creates, tests, and archives build artifacts.

## Topics Covered

- Build artifacts
- Creating files during a Jenkins Pipeline
- Testing generated artifacts
- `archiveArtifacts`
- Artifact fingerprinting
- Accessing archived artifacts from Jenkins

## Practical Implementation

The pipeline creates:

`build/app-info.txt`

The file contains the application name, build information, and timestamp.

The pipeline then verifies that the file exists and archives it using Jenkins.

## Pipeline Flow

Build → Create Artifact → Test → Archive Artifact → Post Actions

## Result

The pipeline completed successfully and the generated artifact was available from the Jenkins build page.

## Key Learning

Jenkins artifacts allow build outputs to be preserved after a pipeline finishes and can be used by later CI/CD processes.
