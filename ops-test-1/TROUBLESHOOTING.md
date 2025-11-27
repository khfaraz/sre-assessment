# TROUBLESHOOTING & Changes

## 1. Application Part (main.py)

Fixed two issues in `main.py` file:

- The home (`/`) endpoint responded very slowly due to an time delay.
- The `/healthz` endpoint returned HTTP 500 even though the service was healthy.

### What was broken

- `time.sleep(random.randint(3,8))`: This causes a 3–8 second delay on every request.
It made the application feel broken or overloaded.
- `jsonify({"status": "ok"}), 500`:  which forced a 500 status code though the service was healthy.
### What I changed

- Removed the line `time.sleep(random.randint(3,8))` from the `/` handler so that it responds fast.
- Changed `/healthz` to return HTTP 200 when healthy ,`return jsonify({"status": "ok"}), 200`.


## How to verify (local)

1. Create and activate the Python virtual environment :

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies :

```bash
pip install -r app/requirements.txt
```
3. Run the application :

```bash
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

## Root cause and recommendation

- Root cause: artificial blocking sleep and incorrect hard-coded HTTP status code. The blocking sleep increases response latency and can cause readiness/liveness probes or clients to time out. The incorrect status code caused orchestration systems to think the service was unhealthy.
- Recommendation: avoid artificial sleeps in request handlers. If simulating latency for testing, do it in separate test code or behind a debug flag. Ensure health endpoints always return an accurate status code (200 for OK). Add unit tests for the health endpoint and automated checks in CI.

## Commands I ran while fixing

- `sed -n '1,160p' app/main.py` (inspect file)
- Edited `app/main.py` to remove `time.sleep(...)` and change health return code.
- `python3 app/main.py` and used `curl` to verify responses.

## Screenshot

Below is the screenshot showing the fix applied to the application:

![Fix applied](./images/fix_application.png)

