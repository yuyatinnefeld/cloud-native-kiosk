# Frontend Flask App

## Debug

1. Run VS Code Debug Mode 'CNK Frontend'

2. 
```bash
python3 -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
flask --app app.main run
```

```bash
curl -X GET http://localhost:5000/home

curl -X GET http://localhost:5000/account

curl -X POST http://localhost:5000/payment
```

## Run & Push Python FE App
```bash
IMAGE_NAME="yuyatinnefeld/python-flask-simple-app"
docker build -t ${IMAGE_NAME} .
docker run -e APP_NAME="hello-fastapi" -it -p 5000:5000 ${IMAGE_NAME}
docker image tag ${IMAGE_NAME} ${IMAGE_NAME}:1.0.0
docker image push ${IMAGE_NAME}:1.0.0
```