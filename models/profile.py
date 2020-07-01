from db import db
from datetime import datetime


class Profile(db.Model):
    __tablename__ = "backend_profile"

    id = db.Column(db.Integer, primary_key=True)
    inserted_date = db.Column(db.DateTime, default=datetime.utcnow)
    report_date = db.Column(db.DateTime)
    is_active = db.Column(db.Boolean, default=True)
    filename = db.Column(db.String(500), nullable=False)
    modelversion_id = db.Column(db.Integer,
                                db.ForeignKey('backend_modelversion.id'),
                                nullable=False)
