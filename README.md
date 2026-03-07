# Containerized Monitoring Service

## Overview

This project implements a minimal monitoring-ready web service using **Python Flask**.  
The service provides health and metrics endpoints and is containerized using **Docker** and deployed locally using **Kubernetes**.

The goal of this project is to demonstrate clean container practices, structured logging, and reproducible deployment.

---

## Architecture

Flask Application  
↓  
Docker Container  
↓  
Kubernetes Deployment  
↓  
Kubernetes Service

The application exposes two endpoints used for monitoring and health checks.

---

## Features

- Health check endpoint
- Metrics endpoint
- Request counting
- Uptime tracking
- Structured JSON logging
- Docker containerization
- Kubernetes deployment
- Reproducible setup

---

## API Endpoints

### Health Endpoint
