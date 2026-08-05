# Jenkins Day 1

## Topics Covered

- Jenkins installation and setup
- Jenkins dashboard
- Freestyle projects
- Jenkins jobs and builds
- Execute Shell build steps
- Jenkins workspace
- Git and GitHub integration
- Branch configuration (`main`)
- Git checkout from GitHub
- Basic CI workflow

## Practical 1 - First Jenkins Job

Created a Freestyle Jenkins job and executed Linux shell commands.

The build successfully returned:

Finished: SUCCESS

## Practical 2 - GitHub + Jenkins

Connected Jenkins to the GitHub repository and configured it to build the `main` branch.

Jenkins successfully:

1. Cloned the GitHub repository
2. Checked out the `main` branch
3. Created the Jenkins workspace
4. Executed `app.sh`
5. Completed the build successfully

## CI Workflow

GitHub
↓
Jenkins
↓
Checkout main
↓
Jenkins Workspace
↓
Execute Shell
↓
Build Result

## Day 1 Result

Jenkins successfully executed code retrieved from GitHub.
