from flask import jsonify

from __init__ import app

""" This module is intended to deliver order information through the API

Relevant calls include '/order', '/order/<int>'
Prepend '/api/v0.1/' to the calls to get the correct path.

Example response:
{
  "type": "order",
  "created_at": "2011-03-19T15:42:22Z",
  "updated_at": "2012-06-14T00:14:27Z",
  "_links": {
    "self": "https://api.moover.io/api/v0.1/order/21229404"
  },
  "image": "http://static-cdn.moover.io/order_images/test_order1-image-6947308654ad603f-300x300.jpeg",
  "_id": 21229404,
  "sender": {
    "_id": "https://api.moover.io/api/v0.1/user/test_user1",
    "address": "asngeuitghnth"
  },
  "receiver": {
    "_id": "https://api.moover.io/api/v0.1/user/test_user2",
    "address": "sfasdfgasdf"
  },
  "moover": "https://api.moover.io/api/v0.1/user/test_user3"
}
"""


@app.route("/api/v0.1/order", methods=["GET"])
def get_orders():
    """ Return the list of orders where the user is either a sender or receiver

    """
    return jsonify({"list of orders"})


@app.route("/api/v0.1/order/<int:order_id>", methods=["GET"])
def get_order(order_id):
    """Return a specific order by its ID

    """
    return jsonify({"a specific order"})


@app.route("/api/v0.1/order", methods=["PUT"])
def add_order():
    """Add an order to the system

    Requires sender and receiver to be set, but not a moover.
    """
    pass
