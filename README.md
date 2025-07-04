# Sentinel — Drift & Model Performance Monitor

**Sentinel** is a lightweight microservice that monitors deployed ML models for **data drift**, **input anomalies**, and **performance drops**.  
It helps catch silent failures in production by validating incoming data and predictions in real time.

---

## 🗂️ Project Scope

- ✅ **Input:** Simulated log stream or API with input features + model predictions
- ✅ **Validation:** Check for schema mismatches, missing values, and basic stats anomalies
- ✅ **Drift Detection:** Simple mean/std or KS test on numeric features
- ✅ **Performance Monitoring:** Rolling accuracy, F1, or confusion matrix (if ground truth available)
- ✅ **Alerts:** Expose alert status via `/alerts` API route or simple dashboard
- ✅ **Dashboard:** Tiny web UI with drift stats, rolling performance, status messages

---

## ⚙️ Tech Stack

- **Backend:** Python 3, FastAPI
- **Drift/Stats:** Pandas, SciPy, NumPy
- **Frontend:** HTMX + Tailwind *or* minimal React/Vite (decide together)
- **Container:** Docker
- **CI/CD:** GitHub Actions (lint, test, build)
- **Infra:** Deploy on Cloud Run, Fly.io, or Render

---

## 📌 MVP Deliverables (Minimum Viable Product)

1. 🏗️ **Schema & Input Validator**
   - Parse incoming data (CSV or JSON)
   - Check columns, types, missing values

2. 📊 **Drift Detector**
   - Calculate mean/std dev for selected features
   - Compare to baseline snapshot
   - Basic KS test for distribution shift

3. ✅ **Performance Checker**
   - Store rolling window of predictions + true labels
   - Compute rolling accuracy / F1

4. 📡 **API Endpoints**
   - `/health` → basic service check
   - `/validate` → run schema check
   - `/drift` → return drift score
   - `/alerts` → return current drift/warning status

5. 🗂️ **Dashboard**
   - Display drift stats & rolling performance visually
   - Auto-refresh or lightweight HTMX partials

6. 🚀 **Infra**
   - Dockerize entire app
   - CI/CD with lint + test pipeline
   - Deploy on any free cloud platform

---

## Dev Setup
```
# 1️⃣ Clone the repo
git clone https://github.com/yourusername/sentinel-ml.git
cd sentinel-ml

# 2️⃣ Create a virtual env
python -m venv .venv

# 3️⃣ Activate it
# macOS/Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate

# 4️⃣ Install project deps
pip install -r requirements.txt

```

---
## 🧩 Team Tasks — Week 1

**Backend:**  
- [ ] `main.py`: FastAPI skeleton with `/health`
- [ ] `validator.py`: Schema & missing value check
- [ ] `drift.py`: Mean/std diff check

**Frontend:**  
- [ ] Pick minimal stack: HTMX or React
- [ ] Design simple single-page status view

**Infra:**  
- [ ] Write `Dockerfile`
- [ ] Set up `.gitignore` + `.dockerignore`
- [ ] Draft `ci.yml` for GitHub Actions lint/test

---

## 📝 How We Work

- 🔀 **Branches:** `main` for stable, `dev` for features
- ✅ **PRs:** Every change must have a clear PR, even for small tests
- 🔒 **Issues:** Use GitHub Issues for bugs, TODOs, enhancements
- 🧪 **Tests:** Write simple unit tests for drift logic & validation checks

---

## 📌 Out of Scope (For Now)

- No fancy model training — focus on monitoring
- No heavy auth, just basic for learning
- No big infra — keep it deployable on any student budget

---

## 📢 Credits

*Sentinel* is a student learning project built by **Chinmay Shet** & **Omkar Shinde**, inspired by real-world data drift monitoring needs.

---

## 🚀 Let’s get started!

