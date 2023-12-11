from blueprints.initialize_blueprints import init_blueprints
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mariadb://pratyush:pratyush@localhost:3306/assignment"

db = SQLAlchemy(app)
init_blueprints(app)

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50))
  email = db.Column(db.String(50),unique=True)

