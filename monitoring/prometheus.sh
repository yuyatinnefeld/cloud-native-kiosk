#!/bin/bash

# add the repo if not exist
# helm repo add prometheus-community https://prometheus-community.github.io/helm-charts

# set the namaspace 'cnk-ns' as default (from argocd/argocd.yaml)
kubectl config set-context --current --namespace $NAME_SPACE

# install the prometheus operator
helm list
helm install prometheus-operator prometheus-community/kube-prometheus-stack --namespace $NAME_SPACE

# check if the crds (custom resource definition) alertmanagers is installed
kubectl get crds

# check the all components
kubectl get all --namespace $NAME_SPACE
