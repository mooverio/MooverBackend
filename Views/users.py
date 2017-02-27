from flask import jsonify

from __init__ import app

""" This module is intended to deliver user information through the API

Relevant calls include '/user', '/user/<int>'
Prepend '/api/v0.1/' to the calls to get the correct path.

Example response:
{
  "type": "user",
  "name": "test_user1",
  "created_at": "2011-03-19T15:42:22Z",
  "updated_at": "2012-06-14T00:14:27Z",
  "_links": {
    "self": "https://api.moover.io/api/v0.1/user/test_user1"
  },
  "image": "http://static-cdn.moover.io/user_images/test_user1-profile_image-6947308654ad603f-300x300.jpeg",
  "_id": 21229404,
  "display_name": "test_user1"
}


"""

@app.route("/api/v0.1/user", methods=["GET"])
def get_user():
    return jsonify({"own userinfo"})

@app.route("/api/v0.1/user/<int:user_id>", methods=["GET"])
def get_user(user_id):
    return jsonify({"userinfo"})