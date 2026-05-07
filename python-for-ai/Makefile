# Bookstore API Makefile

.PHONY: help install test lint format clean docker-build docker-run server stop

# Default target
help:
	@echo "Available commands:"
	@echo "  install      Install dependencies"
	@echo "  test         Run tests"
	@echo "  lint         Run linting tools"
	@echo "  format       Format code with black and isort"
	@echo "  security     Run security checks"
	@echo "  clean        Clean up cache files"
	@echo "  docker-build Build Docker image"
	@echo "  docker-run   Run Docker container"
	@echo "  server       Start development server"
	@echo "  stop         Stop running server"

# Install dependencies
install:
	pip install -r requirements.txt

# Run tests
test:
	python test_bookstore.py

# Run linting
lint:
	flake8 bookstore_api.py test_bookstore.py
	black --check bookstore_api.py test_bookstore.py
	isort --check-only bookstore_api.py test_bookstore.py
	mypy bookstore_api.py test_bookstore.py

# Format code
format:
	black bookstore_api.py test_bookstore.py
	isort bookstore_api.py test_bookstore.py

# Security checks
security:
	bandit -r bookstore_api.py test_bookstore.py
	safety check --file requirements.txt

# Clean cache files
clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete
	rm -rf .mypy_cache .pytest_cache .coverage

# Docker commands
docker-build:
	docker build -t bookstore-api .

docker-run:
	docker run -p 8000:8000 bookstore-api

# Start development server
server:
	python bookstore_api.py

# Stop server (if running in background)
stop:
	pkill -f "python bookstore_api.py" || true