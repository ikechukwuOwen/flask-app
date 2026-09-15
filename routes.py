from app import app, db, login_manager
from flask import Flask, render_template, flash, redirect, url_for, request
from forms import SignUP, Login
from models import User
from flask_login import login_user
from urllib.parse import urlsplit

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

@app.route("/", methods = ["GET", "POST"])
def home():
    return render_template('index.html')


@app.route('/login', methods =["GET", "POST"] )
def login():
    form = Login()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('invalid Username or Password')
            return redirect(url_for('login'))
        login_user(user, remember= form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or urlsplit(next_page).netloc:
            next_page = url_for('home')
        return redirect(next_page) 
    return render_template('login.html', form = form)

@app.route('/sign_up', methods = ["GET", "POST"])
def sign_up():
    form = SignUP()
    if form.validate_on_submit():
        user = User(username = form.username.data, email = form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations You have been registered')
        return redirect(url_for('home_page'))
    return render_template('signup.html', form = form)

@app.route('/home_page', methods = ["GET", "POST"])
def home_page():
    return "<h1> na ndi na acho ike </h1>"