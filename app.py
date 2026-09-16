from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os



app = Flask(__name__)
app.config['SECRET_KEY'] = 'MaziLoli'
database_url = os.environ.get("DATABASE_URL", "sqlite:///loliDB.db")

if database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql://", 1)
app.config['SQLALCHEMY_DATABASE_URI'] = app.config["SQLALCHEMY_DATABASE_URI"] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

import routes