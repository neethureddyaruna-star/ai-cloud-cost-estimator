# AI Powered Cloud Cost Estimator

This project predicts cloud computing costs using an AI model and is deployed using Docker containers and Kubernetes.

## Technologies Used
- Python
- Flask
- Scikit-learn
- Docker
- Kubernetes
- GitHub

## Project Structure

app.py – AI model and API  
requirements.txt – Python dependencies  
Dockerfile – Docker container configuration  
deployment.yaml – Kubernetes deployment configuration  
service.yaml – Kubernetes service configuration  

## Features
- Predicts cloud cost based on CPU, RAM, storage and usage hours
- Containerized using Docker
- Deployable on Kubernetes clusters

## Example Input
{
  "cpu": 4,
  "ram": 8,
  "storage": 100,
  "hours": 200
}
