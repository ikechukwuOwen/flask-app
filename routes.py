from app import app
from flask import Flask, render_template

@app.route("/", methods = ["GET", "POST"])
def home():
    return render_template('index.html')


@app.route('/login', methods =["GET", "POST"] )
def login():
    return "<h1>login</h1>"

@app.route('/sign_up', methods = ["GET", "POST"])
def sign_up():
    return "<h1>SIGN UP</h1>"