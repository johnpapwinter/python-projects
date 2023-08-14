from db import db


class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(500), nullable=False)
    completed = db.Column(db.Boolean, nullable=False)
    date = db.Column(db.Date, nullable=False)
