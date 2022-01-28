from db import db

# Create the User model for sqlAlchemy to work

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Text, unique=True, nullable=False)
    name = db.column(db.Text)
    last_name = db.column(db.Text)
    hash = db.Column(db.Text, nullable=False)