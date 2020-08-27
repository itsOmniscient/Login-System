from login_system import app, db, bcrypt
from flask import Flask, render_template, url_for, redirect, flash
from login_system.forms import RegistrationForm, LoginForm
from login_system.models import User
from flask_login import login_user, login_required, logout_user

@app.route('/')
@app.route('/home')
def home_route():
    return render_template('index.html')

@app.route('/register', methods=('GET', 'POST'))
def register_route():
    form = RegistrationForm()
    if form.validate_on_submit():
        pass_hash = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(name=form.name.data,username=form.username.data,email=form.email.data, password=pass_hash)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('home_route'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login_route():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('home_route'))
        else:
            wrong = 'Please check your username or password.'
            return render_template('login.html', form=form, wrong=wrong)
    return render_template('login.html', form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home_route'))
