from __main__ import app
import requests
from flask import Flask, request, jsonify
from DB.DB import db
from Bugs.bugModel import Bug
from Bugs.bugSchema import bugs_schema,bug_schema

Bug = Bug()
# Routes

@app.route('/', methods=['GET'])
def test():
    return jsonify({"msg": "Hello World"})

# Add Bug Route
@app.route('/report-bug', methods=['POST'])
def addBug():
    report = request.json["report"]
    email = request.json["email"]
    status = "open"
    phone = request.json["phone"]
    new_bug = Bug(report, email, status, phone)

    db.session.add(new_bug)
    db.session.commit()
    resp = requests.get("http://localhost:3002/send-bug-mail")
    return resp.json()

# get all Bugs Route


@app.route("/bug", methods=["GET"])
def get_bugs():
    all_bugs = Bug.query.all()
    result = bugs_schema.dump(all_bugs)
    return jsonify(result)

# get single Bug Route


@app.route("/bug/<id>", methods=["GET"])
def get_bug(id):
    bug = Bug.query.get(id)
    return bug_schema.jsonify(bug)

# Update Bug Route


@app.route('/bug/<id>', methods=['PUT'])
def update_Bug(id):
    bug = Bug.query.get(id)

    description = request.json["description"]
    user = request.json["user"]
    status = request.json["status"]

    bug.description = description
    bug.user = user
    bug.status = status

    db.session.commit()

    return bug_schema.jsonify(bug)

# delete single Bug Route

# @app.route("/bug/<id>", methods=["DELETE"])
# def delete_bug(id):
#     bug = Bug.query.get(id)
#     db.session.delete(bug)
#     db.session.commit()

#     return bug_schema.jsonify(bug)
