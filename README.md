# Containerized Monitoring Service

This project implements a simple monitoring-ready microservice built with Flask.  
The service is containerized using Docker and can be deployed on Kubernetes.

The service exposes health and metrics endpoints and includes a failure detection
and automated recovery mechanism.

---

## Features

- Health monitoring endpoint
- Metrics endpoint with request tracking
- Failure simulation endpoint
- Automated failure detection
- Automatic recovery mechanism
- Structured JSON logging
- Docker containerization
- Kubernetes deployment

---

## API Endpoints

### Health Check

GET /health

Returns service health status.

Example response:

{
 "status": "healthy",
 "timestamp": "2026-03-10T12:00:00"
}

---

### Metrics

GET /metrics

Returns request count and uptime.

Example:

{
 "requests": 5,
 "uptime_seconds": 120,
 "timestamp": "2026-03-10T12:05:00"
}

---

### Simulate Failure

POST /simulate-failure

This endpoint simulates a service failure.

Example:

curl -X POST http://localhost:5000/simulate-failure

Response:

{
 "status": "failure_simulated"
}

---

## Failure Detection and Recovery

The service includes a background monitoring loop that runs every 5 seconds.

When a failure state is detected:

1. The system logs the failure event
2. A recovery attempt is triggered
3. The service state is restored
4. Recovery success is logged

Example log sequence:

failure_simulated  
service_unhealthy_detected  
recovery_attempt  
recovery_successful  

---

## Running Locally

Install dependencies:

pip install -r requirements.txt

Run service:

python app/app.py

Test health:

curl http://localhost:5000/health

Simulate failure:

curl -X POST http://localhost:5000/simulate-failure

---

## Docker Build

Build image:

docker build -t monitoring-service .

Run container:

docker run -p 5000:5000 monitoring-service

---

## Kubernetes Deployment

Apply deployment:

kubectl apply -f k8s/deployment.yaml

Apply service:

kubectl apply -f k8s/service.yaml

Check pods:

kubectl get pods

---

## Architecture

Flask Application  
Monitoring Loop  
Failure Detection  
Automated Recovery  

The monitoring thread continuously checks the service state and triggers
recovery when the service enters a failure condition.

---

## Author

Rayyan Shaikh
