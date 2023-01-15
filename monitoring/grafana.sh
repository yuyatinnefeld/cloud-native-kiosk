#!/bin/bash


# check the service type. (ClusterIP = Internal Service > port-forward necessary)
kubectl get services

# check the grafana pod
POD_NAME=$(kubectl get pods -o=name | grep prometheus-operator-grafana | sed "s/^.\{4\}//")
kubectl describe pod $POD_NAME

# check the grafana logs and note default user and port
kubectl logs $POD_NAME -n prometheus -c grafana

echo "user: admin"
echo "adminPassword: prom-operator"
echo "source: https://github.com/prometheus-community/helm-charts/blob/main/charts/kube-prometheus-stack/values.yaml"

# forward port
kubectl get deployment
PORT=3000
DEPLOYMENT_NAME=prometheus-operator-grafana

kubectl port-forward deployment/$DEPLOYMENT_NAME $PORT