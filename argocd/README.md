# ArgoCD
![Screenshot](/img/argocd_ui.png)

## Setup

```bash
# deploy ArgoCD
bash start_argocd.sh

# access ArgoCD UI
bash open_argocd.sh

open http://localhost:8080
```

### track your git repo
```bash
kubectl apply -f argocd.yaml
```

## Info
- https://argo-cd.readthedocs.io/en/stable/getting_started/
