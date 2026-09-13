from app import app
from flask import Flask, render_template
from forms import SignUP, Login

@app.route("/", methods = ["GET", "POST"])
def home():
    return render_template('index.html')


@app.route('/login', methods =["GET", "POST"] )
def login():
    my_form = Login()
    return render_template('login.html', form = my_form)

@app.route('/sign_up', methods = ["GET", "POST"])
def sign_up():
    my_form = SignUP()
    return render_template('signup.html', form = my_form)