# 🧠 SRE Assessment 2

This assessment evaluates your ability to:

- Diagnose complex issues
- Fix broken production-style systems
- Debug race conditions & memory leaks
- Work with Kubernetes, HPA, Docker multi-stage builds
- Investigate logs and network behavior
- Communicate clearly with incident reporting

Please submit your work through a **public GitHub repository**.

---

# 📂 Project Structure

```
sre-l2-advanced-assessment/
│
├── app/
│   ├── server.go
│   ├── go.mod
│   └── go.sum
│
├── sidecar/
│   └── proxy.py
│
├── Dockerfile
├── docker-compose.yaml
│
├── k8s/
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── hpa.yaml
│   └── networkpolicy.yaml
│
├── logs/
│   ├── app.log
│   └── sidecar.log
│
└── TROUBLESHOOTING.md   (you will fill this)
```

Do not delete or rearrange files.

---

# 🔥 **1. Fix the Go Application (20 points)**

The Go app intentionally includes:

- A memory leak  
- A race condition  
- Latency issues  
- A faulty health endpoint that randomly fails  

Tasks:

- Fix all issues  
- Explain each bug and your fix  
- Add proper logging where missing  

Write your explanation in `TROUBLESHOOTING.md`.

---

# 🐳 **2. Fix the Broken Multi-Stage Dockerfile (10 points)**

Current issues include:

- Missing CA certificates  
- Wrong binary copy path  
- Wrong exposed port  
- No non-root user  
- Inefficient build layer structure  

Deliverables:

- Functional, optimized multi-stage Dockerfile  
- Explanation of changes  

---

# ☸️ **3. Fix the Kubernetes Deployment (15 points)**

Current deployment issues:

- Proper configuration of ports  
- Wrong readinessProbe  
- Poor resource limits (too low)  
- Wrong imagePullPolicy  
- Pod fails due to sidecar conflicts  

You must:

- Fix all YAML  
- Deploy (kind/minikube)
- Verify pod reaches **Ready**  
- Describe each issue and solution  

---

# 📉 **4. Fix the HPA (HorizontalPodAutoscaler) (10 points)**

The HPA does not work.

You must:

- Correct the metrics definition  
- Make autoscaling functional  
- Explain how you validated it  
- Provide CPU load test commands  

---

# 🌐 **5. Fix the Network Issues (Sidecar Debugging) (10 points)**

The sidecar proxy:

- Randomly drops 20% of requests  
- Introduces 3s timeouts  
- Causes 504 gateway errors in the main app  

You must:

- Investigate sidecar logs  
- Identify the root cause  
- Propose fixes (code or config)  
- Explain how you verified your fix  

---

# 📄 **6. Log Analysis (10 points)**

Using:

- `logs/app.log`
- `logs/sidecar.log`

Answer:

- What incidents occurred?
- What was the timeline?
- What is the underlying cause?
- What evidence supports this?

Put your answers in `TROUBLESHOOTING.md`.

---

# 📝 **7. Production-Style Incident Report (10 points)**

Write a professional incident report including:

- Summary  
- Impact  
- Root cause  
- Timeline  
- Fixes applied  
- Preventive actions  
- Monitoring or alerting improvements  

Save as:  
`incident-report.md`

---

# ⭐ Bonus (10 points)

Choose any one (or more):

- Add service mesh (Istio/Linkerd)
- Add Prometheus metrics + Grafana dashboard  
- Add structured logging  
- Add retry/backoff logic  
- Add livenessProbe with thresholds  
- Implement rate-limiting  
- Add GitHub CI workflow  
- Add end-to-end tests 

Document your improvement.

---

# 📤 Submission

1. Push your final solution to **a public GitHub repository**.
2. Include the following in your README:

```
Name:
Email:
Time taken:
Environment used (kind/minikube):
Any assumptions:
```

3. Send us the link.

Good luck — this challenge is intentionally difficult!
