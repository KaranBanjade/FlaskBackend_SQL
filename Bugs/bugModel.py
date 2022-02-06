from DB.DB import db
from datetime import datetime
from flask import Flask, request, jsonify
from __main__ import app
# Bug Class/Model
class Bug(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    report = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.today())


def __init__(self, report, email, phone, status):
    self.report = report
    self.email = email
    self.phone = phone
    self.status = status

