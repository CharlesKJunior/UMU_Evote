# models.py
#from flask_sqlalchemy import SQLAlchemy
#from flask_login import UserMixin

#db = SQLAlchemy()

#class User(UserMixin, db.Model):
 #   id = db.Column(db.Integer, primary_key=True)
 #   username = db.Column(db.String(150), unique=True, nullable=False)
 #   password = db.Column(db.String(150), nullable=False)

#class Vote(db.Model):
 #   id = db.Column(db.Integer, primary_key=True)
  #  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
   # candidate = db.Column(db.String(100), nullable=False)
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

class Candidate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)

class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidate.id'), nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())
