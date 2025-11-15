# 🚀 DevOps CI/CD Demo - Complete End-to-End Pipeline

![Build Status](https://github.com/YuvarajNeelagandan/gcp-devops-cicd-demo/actions/workflows/ci.yml/badge.svg)

## 📋 Table of Contents
- [Overview](#overview)
- [Complete Architecture](#complete-architecture)
- [Project Components](#project-components)
- [How Everything Connects](#how-everything-connects)
- [Getting Started](#getting-started)
- [View Live Pipeline](#view-live-pipeline)

---

## 🎯 Overview

This is a **complete, production-ready DevOps CI/CD pipeline** demonstrating:
- ✅ Automated testing with pytest
- ✅ Continuous Integration with GitHub Actions
- ✅ Test report generation and artifact storage
- ✅ 100% open-source and free

**Perfect for:** QA Engineers, Test Automation Engineers, DevOps beginners

---

## 🏗️ Complete Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     DEVELOPER WORKFLOW                          │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
                    ┌──────────────────┐
                    │  Developer writes│
                    │  code & pushes   │
                    │   to GitHub      │
                    └────────┬─────────┘
                             │
                             ▼
┌────────────────────────────────────────────────────────────────┐
│                    SOURCE CONTROL (GitHub)                      │
│  • Version control with Git                                     │
│  • Code review via Pull Requests                                │
│  • Branch protection rules                                      │
└────────────────────────┬───────────────────────────────────────┘
                         │ (Push/PR trigger)
                         ▼
┌────────────────────────────────────────────────────────────────┐
│           CI/CD PIPELINE (GitHub Actions)                       │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  Step 1: Checkout code                                    │  │
│  └──────────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  Step 2: Setup Python 3.9                                 │  │
│  └──────────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  Step 3: Install dependencies (requirements.txt)          │  │
│  └──────────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  Step 4: Run pytest tests                                 │  │
│  │  • API tests (httpbin.org)                                │  │
│  │  • Unit tests                                              │  │
│  └──────────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  Step 5: Generate HTML test report                        │  │
│  └──────────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  Step 6: Upload test artifacts                            │  │
│  └──────────────────────────────────────────────────────────┘  │
└────────────────────────┬───────────────────────────────────────┘
                         │
                         ▼
┌────────────────────────────────────────────────────────────────┐
│                    RESULTS & FEEDBACK                           │
│  • ✅ Build status badge on README                              │
│  • 📊 Test reports stored as artifacts                          │
│  • 📧 Notifications (can add Slack/Email)                       │
│  • 🔍 Detailed logs for debugging                               │
└────────────────────────────────────────────────────────────────┘
```

---

## 📦 Project Components

### 1. **Source Code**
```
.github/
  └── workflows/
      └── ci.yml          # GitHub Actions CI/CD configuration
tests/
  └── test_sample.py      # Pytest test suite (4 tests)
requirements.txt          # Python dependencies
cloudbuild.yaml           # (Optional) GCP Cloud Build config
README.md                 # This file
.gitignore                # Python gitignore
```

### 2. **Testing Framework**
- **Tool:** pytest
- **Tests:**
  - API endpoint status check
  - JSON response validation
  - HTTP headers verification
  - Unit tests (math operations)
- **Report:** HTML report with pytest-html

### 3. **CI/CD Pipeline**
- **Platform:** GitHub Actions (free)
- **Trigger:** Every push to main branch
- **Duration:** ~20 seconds
- **Artifacts:** Test reports stored for 90 days

### 4. **Monitoring & Reporting**
- Build status visible on GitHub
- Test reports downloadable as artifacts
- Failed tests show detailed logs

---

## 🔗 How Everything Connects

### **Part 1: Development → Version Control**
```
Developer Code → Git Commit → Git Push → GitHub Repository
```

### **Part 2: Continuous Integration**
```
GitHub Push → Trigger GitHub Actions → Run CI/CD Workflow
```

### **Part 3: Automated Testing**
```
CI/CD Workflow → Setup Environment → Install Dependencies → Run Tests
```

### **Part 4: Feedback Loop**
```
Test Results → Generate Reports → Upload Artifacts → Notify Developer
```

### **The Complete Flow:**
1. **Developer** writes code and pushes to GitHub
2. **GitHub** detects the push and triggers Actions
3. **GitHub Actions** spins up a Ubuntu VM
4. **Pipeline** installs Python, dependencies, and runs tests
5. **Tests** execute against API endpoints
6. **Reports** are generated and stored
7. **Status** is updated (✅ pass or ❌ fail)
8. **Developer** sees results and downloads reports if needed

---

## 🚀 Getting Started

### **1. Clone the Repository**
```bash
git clone https://github.com/YuvarajNeelagandan/gcp-devops-cicd-demo.git
cd gcp-devops-cicd-demo
```

### **2. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3. Run Tests Locally**
```bash
pytest -v tests/
```

### **4. Generate HTML Report**
```bash
pytest --html=report.html --self-contained-html tests/
```

### **5. Push Changes (Triggers CI/CD)**
```bash
git add .
git commit -m "Your changes"
git push
```

---

## 📊 View Live Pipeline

**GitHub Actions:** [View Workflows](https://github.com/YuvarajNeelagandan/gcp-devops-cicd-demo/actions)

**Latest Build:** Click the badge at the top of this README

**Test Reports:** Download from Actions → Latest workflow run → Artifacts

---

## 🎓 Key Learning Outcomes

✅ **Version Control:** Git workflow and GitHub collaboration  
✅ **CI/CD:** Automated build and test pipelines  
✅ **Test Automation:** Pytest framework for API and unit testing  
✅ **DevOps Practices:** Infrastructure as Code (YAML config)  
✅ **Monitoring:** Test reports and build status tracking  

---

## 💰 Cost

**Total Cost: $0.00 Forever**
- GitHub Actions: Free (2,000 minutes/month for private repos)
- GitHub Repository: Free
- All tools: Open source

---

## 🔧 Future Enhancements

- [ ] Add code coverage reports (pytest-cov)
- [ ] Add linting (flake8, black)
- [ ] Add security scanning (bandit)
- [ ] Add deployment stage
- [ ] Add Slack/Email notifications
- [ ] Add performance testing

---

## 📝 License

MIT License - Feel free to use for learning and portfolio projects!

---

## 👤 Author

**Yuvaraj Neelagandan**
- GitHub: [@YuvarajNeelagandan](https://github.com/YuvarajNeelagandan)
- Portfolio Project: DevOps CI/CD Pipeline

---

**⭐ Star this repo if you found it helpful!**
