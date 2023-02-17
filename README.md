# Cloud Native Kiosk App on GCP / AWS

## Overview
This GitHub project focuses on learning cloud native technologies and frameworks. The objective is to gain hands-on experience with the latest tools and techniques for building scalable and resilient cloud-based applications. Topics covered include Docker, Kubernetes, GCP, AWS, Terraform, and best practices for security, testing, and CI/CD. The project provides interactive, hands-on learning through practical exercises and real-world scenarios. Whether you're a beginner or experienced developer, this project offers the knowledge and skills needed to become proficient in cloud computing.

## Cloud Native Kiosk (cnk)
The cloud native kiosk is a monorepo project built using the Python frameworks Flask (for the frontend) and FastAPI (for the backend). You can view a live demo of the project on GCP at http://xxx.com. The app has a login system, where guests can browse, search, and add products to the cart, but only registered users can checkout and make payments.

## Project Source Code Documentation
https://yuyatinnefeld.github.io/cloud-native-kiosk


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

## 2. Local Debugging (Cluster)

### Running a Local Cluster (minikube)
```bash
# Deploy a local k8s cluster
minikube start --cpus 2 --memory 8192
minikube profile list
minikube ip

# Enable minikube ingress controller to use ./deploy/ingress.yaml
minikube addons enable ingress

# Verify the ingress controller
kubectl get pods -n ingress-nginx | grep ingress-nginx-controller
```

### Mapping the Local Cluster IP and Domain for Local Access
```bash
vi /etc/hosts
```

```bash
# Host Database
...
192.168.64.40 cnk.com
...
# End of section
```

### 2.1. Debugging Manually
```bash
# Deploy components
kubectl apply -f deploy/k8s/pods.yaml
kubectl apply -f deploy/k8s/service.yaml
kubectl apply -f deploy/k8s/ingress.yaml

# Verify the ingress received the cluster IP
kubectl get ingress --watch

# Open the URL
open http://cnk.com
```

### 2.2. Local Debugging with ArgoCD
![Screenshot](/img/argocd_concept.png)


```bash
# Install ArgoCD in your local k8s-cluster
bash argocd/start_argocd.sh

# Check if pods are available
kubectl get pods --namespace argocd

# Open argocd ui
bash argocd/open_argocd.sh
open http://localhost:8080

# Start to sync argocd+github > deploy application clusters
kubectl apply -f ./argocd/argocd.yaml

# Test with test-local-domain
open http://cnk.com

# Test with forward service
NAME_SPACE="cnk-ns"
PORT=5000
SERVICE_NAME="cnk-service"
kubectl get service -n $NAME_SPACE
kubectl port-forward service/$SERVICE_NAME $PORT -n $NAME_SPACE

open http://localhost:5000
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


## IaC via Terraform

### Providers
- google

### Modules
- api
- gke
- service_account

### Resources
- google_container_cluster
- google_container_node_pool
- google_project_service
- google_service_account

### Outputs
- gke_cluster_sa_email

<!-- BEGIN_TF_DOCS -->
## Requirements

No requirements.

## Providers

No providers.

## Modules

No modules.

## Resources

No resources.

## Inputs

No inputs.

## Outputs

No outputs.
<!-- END_TF_DOCS -->
