'use strict';

const express = require('express');

// Constants
const PORT = 8080;
const HOST = '0.0.0.0';

// App
const app = express();
app.get('/', (req, res) => {
  require('dotenv').config();
  var env   = process.env.NODE_ENV; // "dev", "prod"
  var app_name   = process.env.APP_NAME; // "dev", "prod"

  if(env && app_name) { 
    var message = `APP NAME: ${app_name}, ENV: ${env}`;
  }
  else { 
    var message = `APP NAME: ??? application, ENV: ???`;
  }

  res.send(message);

});

app.listen(PORT, HOST, () => {
  console.log(`Running on http://${HOST}:${PORT}`);
});