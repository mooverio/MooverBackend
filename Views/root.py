from __init__ import app

""" Intended to be a blank response that lists all available API endpoints

Response would be similar to:
{
  "token": {
    "authorization": {
      "scopes": ["user_read"],
      "created_at": "2012-05-08T21:55:12Z",
      "updated_at": "2012-05-17T21:32:13Z"
    },
    "user_name": "test_user1",
    "valid": true
  },
  "_links": {
    "user": "https://api.moover.io/api/v0.1/user"
  }
}

"""

@app.route("/")
@app.route("/index")
def index():
    return "Something"