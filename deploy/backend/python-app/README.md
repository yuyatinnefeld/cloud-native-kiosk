# Run & Push Python BE App
```bash
IMAGE_NAME="yuyatinnefeld/python-fastapi-simple-app"
docker build -t ${IMAGE_NAME} .
docker run -e APP_NAME="hello-fastapi" -it -p 8000:80 ${IMAGE_NAME}
docker image tag ${IMAGE_NAME} ${IMAGE_NAME}:1.0.0
docker image push ${IMAGE_NAME}:1.0.0
```