FROM python:3.11-slim

WORKDIR /app

# Copy only requirements first for caching
COPY app/requirements.txt .

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt gunicorn

# Copy the rest of the application
COPY app/ .

# Create non-root user
RUN groupadd -r app \
    && useradd -r -g app -s /usr/sbin/nologin app \
    && chown -R app:app /app
USER app

EXPOSE 8080

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "2", "main:app"]
