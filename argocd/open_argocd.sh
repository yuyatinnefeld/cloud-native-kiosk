export NAME_SPACE="argocd"
kubectl get service -n $NAME_SPACE

echo "******************* ArgoCD UI OPEN *******************"
echo "USER: admin"
echo "PASSWORD: $(kubectl -n $NAME_SPACE get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d; echo)"


export SERVICE_NAME="argocd-server"
kubectl port-forward service/$SERVICE_NAME -n $NAME_SPACE 8080:443