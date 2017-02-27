#!flask/bin/python
from flask import Flask

app = Flask("mooverBackend")

#Import views
import Views.root

if __name__ == "__main__":
    app.run()