# Incident Report: SRE Assessment Service Outage

**Incident ID:** INC-2025-001  
**Date:** 2025-02-11  
**Severity:** High  
**Status:** Resolved  

---

## Summary

The service had multiple issues causing it to fail:
- The app was slow (taking 7+ seconds to respond)
- Health checks were failing
- The service wouldn't start in Kubernetes
- Different parts were using different port numbers

---

## Impact

- Service wasn't working at all
- Response time was 7+ seconds instead of instant
- Kubernetes pods kept failing and never started
- Anyone trying to use the service got errors

---

## Root Cause

We found **4 main problems**:

**1. Application Code:**
- The `/` endpoint had artificial `sleep(3-8 seconds)` making it slow
- `/healthz` endpoint returned HTTP 500 (error) instead of 200 (success)

**2. Docker Container:**
- Container exposed port 80, but app listened on port 8080
- No proper production server (missing gunicorn)

**3. Kubernetes Deployment:**
- Deployment exposed port 80, app was on 8080 (mismatch!)
- Health check probed port 80 instead of 8080
- No automatic restart if container crashed
- Waited only 2 seconds for app to start (too fast)

**4. Image Name:**
- Dockerfile was named `sre-candidate:latest` but Kubernetes looked for `sre-assessment:latest`

---

## What We Fixed

**Application (`app/main.py`):**
-  Removed the artificial sleep
-  Changed `/healthz` to return HTTP 200 (success)

**Docker (`Dockerfile`):**
-  Changed exposed port to 8080
-  Added gunicorn (production server)
-  Reduced image size
-  Made it run as non-root user

**Kubernetes (`k8s/deployment.yaml`):**
-  Changed container port to 8080
-  Health check now checks port 8080
-  Added automatic restart (liveness probe)
-  Wait 5 seconds for app to start (was 2)
-  Updated image name to match

**Service (`k8s/service.yaml`):**
- Confirmed routing is correct (port 80 → 8080)

---

## How to Prevent This

**Immediate:**
1. Test the `/healthz` endpoint before deploying
2. Make sure ports match everywhere (code, Docker, Kubernetes)
3. Never put artificial delays in code