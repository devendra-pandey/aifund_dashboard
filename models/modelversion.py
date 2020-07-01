from db import db
from datetime import datetime


class Modelversion(db.Model):
    __tablename__ = "backend_modelversion"

    id = db.Column(db.Integer, primary_key=True)
    version = db.Column(db.Float, default=1)
    is_active = db.Column(db.Boolean, default=True)
    inserted_date = db.Column(db.DateTime, default=datetime.utcnow)
    model_id = db.Column(db.Integer,
                         db.ForeignKey('backend_model.id'),
                         nullable=False)
