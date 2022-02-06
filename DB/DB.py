from logging import exception
from __main__ import app
# SQLAlchemy works as sequelize for python
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify
# DB Credentials
db_user = "root"
db_pass = ""
db_name = "facpro_db"
db_host = "127.0.0.1"

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@127.0.0.1/facpro_db"

# Just for Warning in console
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# Init db

try:
    db = SQLAlchemy(app)
    print("Connected to db")
except:
    print("Error In connection")