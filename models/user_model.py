from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    role = db.Column(db.String(50), nullable=False, default='User')
    failed_logins = db.Column(db.Integer, default=0) # Advanced: Brute-force protection
    notes = db.relationship('Note', backref='author', lazy=True)