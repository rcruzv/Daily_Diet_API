from database import db
from flask_login import UserMixin

class Meal(db.Model, UserMixin):
    id          = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name        = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    date        = db.Column(db.DateTime, nullable=False)
    with_in     = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "date": self.date,
            "in diet": self.with_in
        }