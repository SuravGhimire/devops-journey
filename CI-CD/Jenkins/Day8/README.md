# Jenkins Day 8 — Credentials and Secrets Management

## Overview

In Day 8, I learned how to securely manage secrets in Jenkins using the Jenkins Credentials Store.

## Topics Covered

- Jenkins Credentials Store
- Secret Text credentials
- Credential IDs
- `withCredentials`
- Secure environment variables
- Secret masking
- Keeping secrets out of source code

## Practical Implementation

A test Secret Text credential was created in Jenkins with the ID:

`day8-demo-secret`

The Jenkins Pipeline accessed the credential using `withCredentials`.

The actual secret value was never printed to the console. The pipeline only verified that the secret was available by checking its length.

## Pipeline Flow

Build → Load Credential → Use Secret Securely → Test → Post Actions

## Result

The pipeline completed successfully and accessed the Jenkins credential without exposing the secret value.

## Key Learning

Sensitive information should be stored in a secure credentials manager instead of being hardcoded into Jenkinsfiles or committed to Git.
