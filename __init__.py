#!flask/bin/python
from flask import Flask

app = Flask("mooverBackend")

#Import views

if __name__ == "__main__":
    app.run()