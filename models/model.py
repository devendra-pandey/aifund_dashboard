from db import db
from datetime import datetime


class Model(db.Model):
    __tablename__ = "backend_model"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),nullable=False,unique=True)
    description = db.Column(db.String(500),nullable=False)
    inserted_date = db.Column(db.DateTime, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)