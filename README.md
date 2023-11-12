# Cloud Native Kiosk App on GCP / AWS

![Screenshot](/img/cnk-architecture.png)

## Overview
This GitHub project focuses on learning cloud native technologies and frameworks. The objective is to gain hands-on experience with the latest tools and techniques for building scalable and resilient cloud-based applications. Topics covered include Docker, Kubernetes, GCP, AWS, Terraform, and best practices for security, testing, and CI/CD. The project provides interactive, hands-on learning through practical exercises and real-world scenarios. Whether you're a beginner or experienced developer, this project offers the knowledge and skills needed to become proficient in cloud computing.

## Cloud Native Kiosk (cnk)
The cloud native kiosk is a monorepo project built using the Python frameworks Flask (for the frontend) and FastAPI (for the backend). You can view a live demo of the project on GCP at http://xxx.com. The app has a login system, where guests can browse, search, and add products to the cart, but only registered users can checkout and make payments.

## Architecture

#### Container Diagram
![Screenshot](/img/container-diagram.png)


#### Component Diagram
![Screenshot](/img/component-diagram.png)


## Project Source Code Documentation

### [CNK Python Backend Application](https://yuyatinnefeld.com/cloud-native-kiosk/docs/app/routes/users/crud)

## Motivation
The author decided to continue this project for the following reasons:
- To build a modern Python monorepo project with Flask and FastAPI that can serve as a template for your own business cases.
- To gain hands-on experience with cloud native and GitOps tools such as k8s, Prometheus, and ArgoCD.
- To learn about cloud technologies like GCP, AWS, Terraform, and GitHub.

## Application Use Cases
- Users can view items available on the kiosk.
- Users can create and manage their account.
- Users can add items to their shopping cart.

## Requirements and Technology Stack:
- Frontend Framework: Flask
- Backend Framework: FastAPI
- Deployment Manger: Kubernetes
- Continuous Integration Tool: GitHub Actions
- Continuous Delivery Tool: ArgoCD
- Hosting: Google Cloud (with a hybrid cloud setup using GCP, RPi, and AWS)



## 1. Local Debugging (Application)
```bash
cat .vscode/launch.json
```

## 2. Local Testing (Cluster)

### Running a k8s Cluster
```bash
# deploy a local k8s cluster
minikube start --cpus 2 --memory 8192
minikube profile list
minikube ip

# enable minikube ingress controller to use ./deploy/ingress.yaml
minikube addons enable ingress

# verify the ingress controller
kubectl get pods -n ingress-nginx | grep ingress-nginx-controller
```

### Update Local DNS for Local Domain Access
```bash
echo -e "$(minikube ip)\tbookinfo.app" | sudo tee -a /etc/hosts
```

### 2.1. Testing Manually Deployment

```bash
./deploy/k8s/README.md
```

### 2.2. Testing with ArgoCD

```bash
./argocd/REAdME.md
```

## 3. Monitoring
```bash
# install monitoring tool (prometheus + grafana)
bash monitoring/prometheus.sh

# start grafana
bash monitoring/grafana.sh

# open port
open http://localhost:3000
```

## 4. Clean up
```bash
kubectl delete -f deploy/ingress.yaml
kubectl delete -f deploy/service.yaml
kubectl delete -f deploy/pods.yaml

minikube delete --all
```

## Test DB Connection

```bash
# TEST IN CLOUD SHELL
INSTANCE_NAME="cnk-sql-instance"
gcloud sql connect ${INSTANCE_NAME} --user=postgres --quiet

# TEST WITH PROXY

# download the Cloud SQL Proxy
curl -o cloud_sql_proxy https://dl.google.com/cloudsql/cloud_sql_proxy.darwin.amd64

# make the proxy executable
chmod +x cloud_sql_proxy

# create proxy connection
./cloud_sql_proxy -instances=${INSTANCE_NAME}=tcp:3306

```
