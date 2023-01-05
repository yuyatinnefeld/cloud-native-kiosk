# cloud-native-kiosk

## About
The cloud native kiosk is a monorepo project for selling kiosk items built by Flask + FastAPI framework. You may see live demo of this project on GCP from the following link. https://xxxx.com. This App has login system functionality. The guest user is able to browse, search and add product to cart only. Checkout and payment option is available for registerd users. The main goal of the project is that you can use this repo as a template for your business case.

## Tech Stack:
- Frontend Framework: Flask
- Backend Framework: FastAPI
- Deployment Manger: Kubernetes
- Continuous Integration Tool: GitHub Actions
- Continuous Delivery Tool: ArgoCD
- Hosting: Google Cloud -> Hybrid Cloud (GCP + RPi + AWS)
## Local Debugging

```bash
# flask app debug
cd src/frontend
pip install -r requirements.txt
export FLASK_APP=app.main.py
flask run

# deployment debug
minikube start --cpus 2 --memory 8192
kubectl apply -f deploy/frontend/app.yaml

# test
kubectl get service
PORT=5000
SERVICE_NAME="flask-service"
kubectl port-forward service/$SERVICE_NAME $PORT

# clean up
kubectl delete -f deploy/frontend/app.yaml
```

## Local Push Image
```bash
export IMAGE_NAME_1=yuyatinnefeld/cloud-native-kiosk-frontend:1.0.0
docker build -t $IMAGE_NAME_1 -f deploy/frontend/Dockerfile .
docker push $IMAGE_NAME_1
```

