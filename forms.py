from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField

class SignUP(FlaskForm):
    username = StringField('Username')
    email = StringField('Email')
    password = PasswordField('Password')
    password2 = PasswordField('Repeat Password')
    submit = SubmitField('Register')

class Login(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    submit = SubmitField('Login')