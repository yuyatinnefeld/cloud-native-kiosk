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
  var dbProvider   = process.env.DB; // "dev", "prod"

  if(env && app_name) { 
    var message = `APP NAME: ${app_name}, ENV: ${env}`;
  }
  else { 
    var message = `APP NAME: ??? application, ENV: ???`;
  }

  if (dbProvider){
    console.log(`Try to Connect DB: ${dbProvider}`)

    const MongoClient = require('mongodb').MongoClient;
    const assert = require('assert');

    const url = 'mongodb://admin:password@mongodb:27017'; // NOT localhost -> mongodb

    const dbName = 'hello';
    
    MongoClient.connect(url, function(err, client) {
      assert.equal(null, err);
      console.log("Connected successfully to server");
    
      const db = client.db(dbName);
    
      client.close();
    });

  }

  res.send(message);

});

app.listen(PORT, HOST, () => {
  console.log(`Running on http://${HOST}:${PORT}`);
});