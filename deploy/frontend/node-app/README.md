# Setup

## Local Deploy
```bash
# 1. create npm project
npm init

# 2. install packages
npm install dotenv express pg

# 3. run node server
NODE_ENV=test-yu DB=mongodb node app.js

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
docker run -e APP_NAME="cnk-node-app" -it -p 8080:8080 ${IMAGE_NAME}
open http://localhost:8080/
docker image tag ${IMAGE_NAME} ${IMAGE_NAME}:1.0.0
docker image push ${IMAGE_NAME}:1.0.0
```

## Dockercompose
```bash
docker-compose build
docker-compose up -d

# check
docker-compose logs mongodb
docker-compose logs mongo-express

# check 2
open http://0.0.0.0:8080
open http://0.0.0.0:8081

# clean up
docker-compose down
docker-compose rm

```
