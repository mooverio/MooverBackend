from __init__ import app
from flask import jsonify


""" This module is intended to deliver user information through the API

Relevant calls include '/user', '/user/<int>'
Prepend '/api/v0.1/' to the calls to get the correct path.

Example response:



"""

@app.route("/api/v0.1/user", methods=["GET"])
def get_user():
    return jsonify({"own userinfo"})

@app.route("/api/v0.1/user/<int:user_id>", methods=["GET"])
def get_user(user_id):
    return jsonify({"userinfo"})