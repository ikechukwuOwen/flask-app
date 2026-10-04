from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
import os
from datetime import timedelta
from flask_migrate import Migrate


app = Flask(__name__)
app.config.update(
    MAIL_SERVER=os.environ.get("MAIL_SERVER", "smtp-relay.brevo.com"),
    MAIL_PORT=int(os.environ.get("MAIL_PORT", 587)),
    MAIL_USE_TLS=True,
    MAIL_USERNAME=os.environ.get("MAIL_USERNAME"),
    MAIL_PASSWORD=os.environ.get("MAIL_PASSWORD"),
    MAIL_DEFAULT_SENDER=os.environ.get("MAIL_DEFAULT_SENDER"),
)
mail = Mail(app)

app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-only-key")

import os

database_url = os.environ.get("DATABASE_URL", "sqlite:///loliDB.db")

if database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql+psycopg://", 1)
elif database_url.startswith("postgresql://"):
    database_url = database_url.replace("postgresql://", "postgresql+psycopg://", 1)

app.config["SQLALCHEMY_DATABASE_URI"] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["REMEMBER_COOKIE_DURATION"] = timedelta(days=30)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager()
login_manager.init_app(app)

import routes