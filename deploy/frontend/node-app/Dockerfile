FROM node:20

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install && npm install mongodb

COPY . .

ENV NODE_ENV=prod APP_NAME="${APP_NAME}"

EXPOSE 8080

CMD ["npm", "run", "start:dev"]