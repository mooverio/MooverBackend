#!flask/bin/python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask("mooverBackend")
app.config.from_object('config')
db = SQLAlchemy(app)

#Import views

if __name__ == "__main__":
    app.run()