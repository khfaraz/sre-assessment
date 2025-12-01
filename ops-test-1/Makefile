.PHONY: help build run test clean deploy-local deploy-k8s

help:
	@echo "Available commands:"
	@echo "  make build          - Build Docker image"
	@echo "  make run            - Run app locally (requires Python venv)"
	@echo "  make test           - Test app endpoints with curl"
	@echo "  make clean          - Remove Docker image and cleanup"
	@echo "  make deploy-local   - Deploy to local kind cluster"
	@echo "  make deploy-k8s     - Deploy to Kubernetes"
	@echo "  make logs           - Show pod logs"
	@echo "  make stop           - Stop local kind cluster"

# Build Docker image
build:
	@echo "Building Docker image: sre-assessment:latest"
	docker build -t sre-assessment:latest .
	@echo "✅ Image built successfully"

# Run app locally
run:
	@echo "Starting app on http://127.0.0.1:8080"
	python3 app/main.py

# Test endpoints
test:
	@echo "Testing endpoints..."
	@curl -s http://127.0.0.1:8080/ && echo " ✅ / is working"
	@curl -s http://127.0.0.1:8080/healthz | grep -q "ok" && echo "✅ /healthz is working"

# Clean up
clean:
	@echo "Cleaning up Docker image..."
	docker rmi sre-assessment:latest 2>/dev/null || true
	@echo "✅ Cleanup complete"

# Deploy to local kind cluster
deploy-local:
	@echo "Creating kind cluster..."
	kind create cluster --name sre-test || true
	@echo "Loading Docker image into kind..."
	kind load docker-image sre-assessment:latest --name sre-test
	@echo "Applying Kubernetes manifests..."
	kubectl apply -f k8s/deployment.yaml
	kubectl apply -f k8s/service.yaml
	@echo "⏳ Waiting for deployment to be ready..."
	kubectl rollout status deployment/sre-app
	@echo "✅ Deployment ready!"
	@echo "Forward port: kubectl port-forward svc/sre-service 8080:80"

# Deploy to current Kubernetes cluster
deploy-k8s:
	@echo "Applying Kubernetes manifests..."
	kubectl apply -f k8s/deployment.yaml
	kubectl apply -f k8s/service.yaml
	@echo "⏳ Waiting for deployment..."
	kubectl rollout status deployment/sre-app
	@echo "✅ Deployment complete!"

# Show pod logs
logs:
	@echo "Fetching logs from pods..."
	kubectl logs -f deployment/sre-app

# Stop local kind cluster
stop:
	@echo "Deleting kind cluster..."
	kind delete cluster --name sre-test
	@echo "✅ Cluster deleted"

# Install dependencies
install:
	@echo "Installing Python dependencies..."
	python3 -m pip install -r app/requirements.txt
	@echo "✅ Dependencies installed"

# Full workflow: build, load to kind, deploy
full-test: build deploy-local
	@echo "✅ Full test complete! Run: kubectl port-forward svc/sre-service 8080:80"
