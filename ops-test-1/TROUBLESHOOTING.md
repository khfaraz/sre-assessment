# TROUBLESHOOTING & Changes

## 1. Application Part (main.py)

Fixed two issues in `main.py` file:

- The home (`/`) endpoint responded very slowly due to an artificial time delay.
- The `/healthz` endpoint returned HTTP 500 even though the service was healthy.

### What was broken

- `time.sleep(random.randint(3,8))`: This causes a 3–8 second delay on every request. It made the application feel broken or overloaded.
- `jsonify({"status": "ok"}), 500`: which forced a 500 status code though the service was healthy.

### What I changed

- Removed the line `time.sleep(random.randint(3,8))` from the `/` handler so that it responds fast.
- Changed `/healthz` to return HTTP 200 when healthy: `return jsonify({"status": "ok"}), 200`.


## How to verify (local)

1. Create and activate the Python virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r app/requirements.txt
```

3. Run the application:

```bash
python3 app/main.py
```

4. Test the endpoints:

```bash
curl -sv http://127.0.0.1:8080/
curl -sv http://127.0.0.1:8080/healthz
```

## Screenshot

Below is the screenshot showing the fix applied to the application:

![Fix applied](./images/fix_application.png)

## 2. Docker Part (Dockerfile)

Fixed multiple issues in the `Dockerfile`:

- Dockerfile not building due to incorrect port and missing WSGI server.
- Inefficient image (no optimization for layer caching and size).
- Minor build problems (incorrect workdir, missing user permissions).

### What was broken

- `WORKDIR /src` and `COPY app .` created path mismatches; app files were copied to wrong location.
- `EXPOSE 80` did not match the application listening on port 8080 (see `app/main.py`).
- No production WSGI server; Flask development server used, which is not suitable for containers.
- Running as root user (security risk).
- `pip install` did not use `--no-cache-dir`, inflating image size.

### What I changed

- Set `WORKDIR` to `/app` and changed `COPY app .` to `COPY app/ /app/` for clarity.
- Exposed port `8080` to match the application.
- Added `gunicorn` as production WSGI server in `requirements.txt` installation and CMD.
- Created non-root `app` user and set proper file ownership.
- Added `pip install --no-cache-dir` to reduce image size.
- Set `PYTHONUNBUFFERED=1` for immediate log output in containers.

### New Dockerfile

```dockerfile
FROM python:3.11-slim

# Environment
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Copy application code
COPY app/ /app/

# Install dependencies and production server (gunicorn)
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt gunicorn

# Create non-root user and set ownership
RUN groupadd -r app && useradd -r -g app app \
    && chown -R app:app /app

USER app

# The application listens on port 8080 (see app/main.py)
EXPOSE 8080

# Use gunicorn for production-like serving; main.py exposes `app` WSGI callable
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "2", "main:app"]
```

## How to build and verify (local)

1. Build the Docker image:

```bash
docker build -t sre-assessment:latest .
```

2. Run the container:

```bash
docker run --rm -p 8080:8080 sre-assessment:latest
```

3. Test the endpoints (in another terminal):

```bash
curl -sv http://127.0.0.1:8080/
curl -sv http://127.0.0.1:8080/healthz
```

Expected output:
- `/`: Returns "Hello from SRE Test!" quickly.
- `/healthz`: Returns HTTP 200 with JSON `{"status":"ok"}`.

## Root cause and recommendations

- Root cause: Mismatch between exposed port (80) and app port (8080), missing production server, and suboptimal image practices.
- Recommendations: 
  - Pin package versions in `app/requirements.txt` for reproducible builds.
  - Add `HEALTHCHECK` directive to the Dockerfile for orchestration systems.
  - Consider multi-stage builds if build-time dependencies are later needed.
  - Use `.dockerignore` to exclude unnecessary files during copy operations.

