# Run & Push Golang App
```bash
export IMAGE_NAME="yuyatinnefeld/golang-simple-app"
docker build -t ${IMAGE_NAME} .
docker run -e APP_NAME="hello-world-app" -it -p 9999:9999 ${IMAGE_NAME}
docker image tag ${IMAGE_NAME} ${IMAGE_NAME}:1.0.0
docker image push ${IMAGE_NAME}:1.0.0
```