# 🔧 SRE Assessment 1

Welcome to the SRE Level-1 assessment.  
This test is designed to evaluate your skills in:

- Docker
- Kubernetes basics
- Debugging & troubleshooting
- Understanding logs
- Applying fixes to a small service
- Communication & documentation

Please follow all instructions carefully and submit your work in a **public GitHub repository**.

---

# 🧪 Overview

You are given a small, intentionally broken service.

Your tasks:

1. Fix the application  
2. Fix the Dockerfile  
3. Fix the Kubernetes deployment  
4. Deploy locally using **kind** or **minikube**  
5. Analyze provided logs  
6. Write an incident report  
7. Document your debugging steps  

---

# 📂 Project Structure

```
sre-l1-assessment/
│
├── app/
│   ├── main.py
│   └── requirements.txt
│
├── Dockerfile
│
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
│
├── logs.txt
│
└── TROUBLESHOOTING.md   (you will fill this)
```

You should NOT modify the initial structure.

---

# ✅ **1. Fix the Application (10 points)**

Located in: `app/main.py`

Issues you must identify and fix:

- The home ("/") endpoint responds very slowly  
- The `/healthz` endpoint returns the **wrong HTTP status code**  

**Deliverables:**

- Working application
- Explanation of what was broken and what you changed (in TROUBLESHOOTING.md)

---

# 🐳 **2. Fix the Dockerfile (10 points)**

Issues include:

- Dockerfile not building
- Inefficient image  
- Minor build problems  

**Deliverables:**

- A working, optimized Docker image  
- Explanation of changes  

---

# ☸️ **3. Fix the Kubernetes Deployment (15 points)**

Located in: `k8s/deployment.yaml` and `k8s/service.yaml`

The Kubernetes deployment has multiple issues:

- Deployed application is not running
- Readiness probe fails  
- Service not routing properly  

You must:

- Fix all YAML issues  
- Deploy locally (`kind` or `minikube`)  
- Verify service is reachable
- Give an explanation of Readiness and Liveness uses 

**Deliverables:**

- Working deployment  
- Notes of problems identified and how you fixed them  

---

# 📄 **4. Debug logs.txt (10 points)**

The provided logs indicate probe failures and latency issues.

In your own words, answer:

- What caused the readiness probe failures?  
- Why is the service slow?  
- What is the probable root cause?  
- What permanent fix would resolve it?  

Write your answers in **TROUBLESHOOTING.md**.

---

# 📝 **5. Incident Report (10 points)**

Write a short incident report that includes:

- **Summary**  
- **Impact**  
- **Root cause**  
- **What you fixed**  
- **Preventive actions**  

Format must be clear and concise.

Put this in a file named:  
`incident-report.md`

---

# 📘 **6. Documentation (10 points)**

Update the provided `TROUBLESHOOTING.md` with:

- Step-by-step process you followed  
- Commands you ran  
- Screenshots (optional)  
- What you learned  

This helps us understand your thinking process.

---

# ⭐ Bonus (5 points)

Do **any** one improvement (or more):

- Add resource requests/limits  
- Add a livenessProbe  
- Add autoscaling (HPA)  
- Add Makefile for automation  
- Add GitHub CI for lint/build  
- Add Prometheus metrics 
- Deploy an Ingress Controller with proper Load Balancer Configuration 

Include your reasoning.

---

# 📤 Submission

1. Push your final solution to a **public GitHub repository**.
2. Include this in the README of your repo:

```
Name:
Email:
Time taken:
Any assumptions:
```

3. Share the GitHub link with us.

Good luck!
