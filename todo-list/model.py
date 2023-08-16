from db import db


class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(500), nullable=False)
    completed = db.Column(db.Boolean, nullable=False)
    date = db.Column(db.Date, nullable=False)

    def __str__(self):
        return f"id: {self.id}, description: {self.description}, completed: {self.completed}, date: {self.date}"
