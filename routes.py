from app import app, db, login_manager
from flask import  render_template, flash, redirect, url_for, request
from forms import SignUP, Login, CreateGroup, JoinGroup
from models import User, Group
from flask_login import login_user, login_required, current_user, logout_user
from urllib.parse import urlsplit


@app.route("/", methods = ["GET", "POST"])
def home():
    return render_template('index.html')


@app.route('/login', methods =["GET", "POST"] )
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home_page'))
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
    if current_user.is_authenticated:
            return redirect(url_for('home_page'))
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
@login_required
def home_page():
    user = User.query.filter_by( username = current_user.username).first()
    return render_template('home.html', user = user.username, group = False)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))

@app.route('/user/<username>', methods = ["GET", "POST"])
@login_required
def user(username):
    user = User.query.filter_by(username= username).first()
    group = Group.query.filter(Group.members.contains(user)).all()

    return render_template('user.html', user = user, group = group)

@app.route('/create_group', methods = ["GET", "POST"])
@login_required
def create_group():
    form = CreateGroup()
    if form.validate_on_submit():
        group = Group(name=form.groupname.data, description=form.description.data, owner_id=current_user.id)
        group.generate_group_code()  # Generate a unique group code
        db.session.add(group)
        db.session.commit()
        flash('Group created successfully!')
        return redirect(url_for('home_page'))
    return render_template('create_group.html', form=form)

@app.route('/join_group', methods = ["GET", "POST"])
@login_required
def join_group():
    form = JoinGroup()
    if form.validate_on_submit():
        group = Group.query.filter_by(name=form.groupname.data).first()
        if group is None or group.code != form.groupcode.data:
            flash('Invalid group name or code')
            return redirect(url_for('join_group'))
        if group.is_private:
            flash('This is a private group. Please contact the owner.')
            return redirect(url_for('join_group'))
        if current_user in group.members:
            flash('You are already a member of this group.')
            return redirect(url_for('join_group'))
        group.members.append(current_user)
        db.session.commit()
        flash('You have joined the group successfully!')
        return redirect(url_for('home_page'))
    return render_template('join_group.html', form=form)

@app.route('/group/<int:group_id>', methods=["GET", "POST"])
@login_required
def group_page(group_id):
    group = Group.query.get_or_404(group_id)
    if current_user not in group.members and current_user != group.owner:
        flash('You are not a member of this group.')
        return redirect(url_for('home_page'))
    return render_template('group.html', group=group)