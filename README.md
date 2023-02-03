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

## Local Debugging (Application)
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
```

## Local Debugging (Deployment)
![Screenshot](/img/argocd_concept.png)

## Run a cluster
```bash
# deployment local k8s cluster
minikube start --cpus 2 --memory 8192
```

## Deploy GitOps Tool (ArgoCD)
```bash
# install argocd in your local k8s-cluster
bash argocd/start_argocd.sh

# open argocd ui
bash argocd/open_argocd.sh
open http://localhost:8080

# start to sync argocd+github > deploy application clusters
kubectl apply -f ./argocd/argocd.yaml

# test
NAME_SPACE="cnk-ns"
PORT=5000
SERVICE_NAME="cnk-service"
kubectl get service -n $NAME_SPACE
kubectl port-forward service/$SERVICE_NAME $PORT -n $NAME_SPACE

open http://localhost:5000
```

## Monitoring
```bash
# install monitoring tool (prometheus + grafana)
bash monitoring/prometheus.sh

# start grafana
bash monitoring/grafana.sh

# open port
open http://localhost:3000
```

## Clean up
```bash
kubectl delete -f deploy/frontend/app.yaml
minikube delete --all
```