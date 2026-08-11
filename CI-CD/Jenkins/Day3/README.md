# Jenkins Day 3 – GitHub Webhooks with ngrok

## 📖 Overview

On Day 3, I configured GitHub Webhooks to automatically trigger Jenkins builds whenever code is pushed to the GitHub repository. Since Jenkins was running locally, I used **ngrok** to expose my local server to the internet, allowing GitHub to communicate with Jenkins.

---

## 📚 Topics Covered

- GitHub Webhooks
- Poll SCM vs Webhooks
- ngrok installation and configuration
- Exposing localhost securely
- Jenkins webhook configuration
- Automatic build triggering
- End-to-end CI workflow

---

## 🛠 Practical

- Installed ngrok
- Connected ngrok with authentication token
- Exposed Jenkins running on localhost
- Configured GitHub Webhook
- Enabled **GitHub hook trigger for GITScm polling**
- Verified automatic Jenkins build after Git push

---

## 🔄 CI Workflow

```text
Developer
    │
git push
    │
    ▼
GitHub Repository
    │
Webhook
    │
    ▼
ngrok Tunnel
    │
    ▼
Local Jenkins
    │
Checkout Repository
    │
Execute Build
    │
Build Success
```

---

## 📁 Folder Structure

```
Day3/
├── notes.txt
├── README.md
```

---

## 🎯 Learning Outcome

By the end of Day 3, I understood how modern CI systems automatically react to source code changes using GitHub Webhooks instead of scheduled polling. I successfully built an event-driven Jenkins workflow where every Git push automatically starts a new Jenkins build.

---

## 🚀 Next Step

Day 4: Jenkins Pipeline & Jenkinsfile (Pipeline as Code)
