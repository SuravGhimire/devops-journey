## Jenkins Day 2

### Topics Covered

- Build Triggers
- Poll SCM
- Automatic Build Detection
- Git Push Workflow

### Practical

Configured Poll SCM using:

H/5 * * * *

After pushing new code to GitHub, Jenkins detected the change and automatically executed the build.

Workflow:

Developer
↓
Git Push
↓
GitHub
↓
Jenkins Poll SCM
↓
Automatic Build
↓
SUCCESS
