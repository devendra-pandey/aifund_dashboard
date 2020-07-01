from db import db
from datetime import datetime


class Stock(db.Model):
    __tablename__ = "backend_stock"

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.Integer, default=0)
    name = db.Column(db.String(400))
    model_decision = db.Column(db.String(20))
    exchange_token = db.Column(db.Integer, default=0)
    instrument_token = db.Column(db.Integer, default=0)
    stop_loss = db.Column(db.Float, default=0)
    stop_gain = db.Column(db.Float, default=0)
    triggered = db.Column(db.String(50))
    previous_close = db.Column(db.Float, default=0)
    today_open = db.Column(db.Float, default=0)
    today_close = db.Column(db.Float, default=0)
    delta_previous_today = db.Column(db.Float, default=0)
    actual_delta = db.Column(db.Float, default=0)
    return_generated = db.Column(db.Float, default=0)
    quantity = db.Column(db.Float, default=0)
    quantity_adjusted = db.Column(db.Float, default=0)
    total_return = db.Column(db.Float, default=0)
    transaction_value = db.Column(db.Float, default=0)
    new_transaction_value = db.Column(db.Float, default=0)
    traditional_brokerage = db.Column(db.Float, default=0)
    zerodha_brokerage = db.Column(db.Float, default=0)
    hybrid_brokerage = db.Column(db.Float, default=0)
    tra_traditional_brokerage = db.Column(db.Float, default=0)
    tra_zerodha_brokerage = db.Column(db.Float, default=0)
    tra_hybrid_brokerage = db.Column(db.Float, default=0)
    is_active = db.Column(db.Boolean, default=True)
    inserted_date = db.Column(db.DateTime, default=datetime.utcnow)
    profile_id = db.Column(db.Integer,
                           db.ForeignKey('backend_profile.id'),
                           nullable=False)
