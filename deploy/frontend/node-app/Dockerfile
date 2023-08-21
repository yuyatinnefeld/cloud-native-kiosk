FROM node:20

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install

RUN npm install pm2 -g

COPY . .

ENV NODE_ENV=prod APP_NAME="${APP_NAME}"

EXPOSE 8080

CMD ["pm2-runtime", "app.js"]