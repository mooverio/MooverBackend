from __init__ import db


class User(db.model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    display_name = db.Column(db.String(64), index=True)
    creation_date = db.Colum(db.DateTime)
