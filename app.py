from blueprints.initialize_blueprints import init_blueprints
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mariadb://pratyush:pratyush@localhost:3306/assignment"

db = SQLAlchemy(app)
init_blueprints(app)

class User(db.Model):
  __tablename__ = "User"
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50))
  email = db.Column(db.String(50),unique=True)

class Posts(db.Model):
  __tablename__ = "Posts"
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(50))
  content = db.Column(db.String(500))
  comments = db.relationship("Comments",backref='Posts')
  likes = db.relationship("Likes",backref='Posts')

class Comments(db.Model):
  __tablename__ = "Comments"
  id = db.Column(db.Integer, primary_key=True)
  comment = db.Column(db.String(500))
  timestamp = db.Column(db.DateTime,default=datetime.datetime.now())
  post_id = db.Column(db.Integer,db.ForeignKey('Posts.id'))

class Likes(db.Model):
  __tablename__ = "Likes"
  id = db.Column(db.Integer, primary_key=True)
  likes = db.Column(db.Integer)
  timestamp = db.Column(db.DateTime,default=datetime.datetime.now())
  post_id = db.Column(db.Integer,db.ForeignKey('Posts.id'))

app.app_context().push()
db.create_all()