FROM python:3.11-slim

WORKDIR /app

# Copy only requirements first
COPY app/requirements.txt .

# install dependencies with gunicorn
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt gunicorn

# Copy the rest of the application
COPY app/ .

# Create non-root user 'kamrul'
RUN groupadd -r kamrul \
    && useradd -r -g kamrul -s /usr/sbin/nologin kamrul \
    && chown -R kamrul:kamrul /app
USER kamrul


EXPOSE 8080

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "2", "main:app"]
