#!/bin/bash


export NAME_SPACE="argocd"
kubectl create namespace $NAME_SPACE
kubectl apply -n $NAME_SPACE -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
kubectl get pods -n $NAME_SPACE
