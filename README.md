# Cloud Native Kiosk App on GCP / AWS

## About
 The cloud native kiosk is a monorepo project for selling kiosk items built by Flask + FastAPI framework. You may see a live demo of this project on GCP from the following link. https://xxxx.com. This App has login system functionality. The guest user is able to browse, search and add product to cart only. Checkout and payment option is available for registerd users. 

## Motivation
I decided to continue the project for the following reasons:
- I wanted to build a modern Python monorepo project with Flask and FastAPI which you can use as a template for your business case.
- I wanted to use cloud native and GitOps tool like k8s, Prometheus, argoCD in practice.
- I enjoy learning more cloud technology like GCP, AWS, Terraform, Github

## Application Use Cases
- users can see kiosk items
- users can create and manage their account
- users can add items to shopping cart

## Requirements and Tech Stack Choices:
- Frontend Framework: Flask
- Backend Framework: FastAPI
- Deployment Manger: Kubernetes
- Continuous Integration Tool: GitHub Actions
- Continuous Delivery Tool: ArgoCD
- Hosting: Google Cloud -> Hybrid Cloud (GCP + RPi + AWS)

## Local Debugging
```bash
# frontend flask app debug
cd deploy/frontend
pip install -r requirements.txt
export FLASK_APP=app.main.py
flask run

# backend fastapi app debug
cd deploy/backend
pip install -r requirements.txt
uvicorn app.main:app --reload

# deployment debug
minikube start --cpus 2 --memory 8192
kubectl apply -f deploy/frontend/app.yaml

# test
kubectl get service
PORT=5000
SERVICE_NAME="flask-service"
kubectl port-forward service/$SERVICE_NAME $PORT

# clean up
kubectl delete -f deploy/frontend/app.yaml
minikube delete --all
```

## Local Pull Image
```bash
export FE_IMAGE_NAME_1=yuyatinnefeld/cloud-native-kiosk-frontend:1.0.0
docker pull FE_IMAGE_NAME_1

export BE_IMAGE_NAME_1=yuyatinnefeld/cloud-native-kiosk-backend:1.0.0
docker pull BE_IMAGE_NAME_1
```

