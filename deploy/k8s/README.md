# Local Deploy & Test

```bash
# deploy components
kubectl apply -f deploy/k8s/app

# verify
kubectl get pod
kubectl get service

# check apps
PORT=8000
SERVICE_NAME="python-be-1-service"
kubectl port-forward service/$SERVICE_NAME $PORT

PORT=5000
SERVICE_NAME="python-fe-1-service"
kubectl port-forward service/$SERVICE_NAME $PORT

PORT=5001
SERVICE_NAME="python-fe-2-service"
kubectl port-forward service/$SERVICE_NAME $PORT

PORT=5678
SERVICE_NAME="http-banana-service"
kubectl port-forward service/$SERVICE_NAME $PORT

# deploy ingress rules
kubectl apply -f deploy/k8s/ingress.yaml

# Verify the ingress received the cluster IP
kubectl get ingress --watch

# Open the URL
open http://cnk.com
```