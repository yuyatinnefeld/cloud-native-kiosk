# ArgoCD
![Screenshot](/img/argocd_ui.png)

## Setup

```bash
# Install ArgoCD in your local k8s-cluster
bash argocd/start_argocd.sh

# Check if all pods are available
kubectl get pods --namespace argocd --watch

# Open argocd UI
bash argocd/open_argocd.sh
open http://localhost:8080

# Start to sync argocd+github > deploy application clusters
kubectl apply -f ./argocd/argocd.yaml

# Test with test-local-domain
open http://cnk.com
```


## Info
- https://argo-cd.readthedocs.io/en/stable/getting_started/
