# Setup

## Local Deploy
```bash
# 1. create npm project
npm init

# 2. install packages
npm install dotenv

# 3. run node server
node app.js # option 1
npm run start:dev # option 2
npm run start:prod # option 3

open http://localhost:8080/
```

## Deploy with pm2

```bash
# install pm2
npm install pm2@latest

# start with pm2
npm run start:pm2:dev

# stop
npm run stop:pm2
```

## Docker Run & Push
```bash
export IMAGE_NAME="yuyatinnefeld/cnk-node-app"
docker build -t ${IMAGE_NAME} .
docker run -e APP_NAME="cnk-node-app" -it -p 8888:8080 ${IMAGE_NAME}
open http://localhost:8888/
docker image tag ${IMAGE_NAME} ${IMAGE_NAME}:1.0.0
docker image push ${IMAGE_NAME}:1.0.0
```