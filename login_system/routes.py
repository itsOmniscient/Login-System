from login_system import app, db, bcrypt, mail
from flask import Flask, render_template, url_for, redirect, flash
from login_system.forms import RegistrationForm, LoginForm, PasswordReset, NewPassword
from login_system.models import User
from flask_login import login_user, login_required, logout_user, current_user
from flask_mail import Message

@app.route('/')
@app.route('/home')
def home_route():
    return render_template('index.html')

@app.route('/register', methods=('GET', 'POST'))
def register_route():
    if current_user.is_authenticated:
        return redirect(url_for('home_route'))
    form = RegistrationForm()
    if form.validate_on_submit():
        pass_hash = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(name=form.name.data,username=form.username.data,email=form.email.data, password=pass_hash, confirmed=False)
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

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset', sender='localhost@dontreply.com', recipients=[user.email])
    msg.body = f'''Password reset link: {url_for('new_password_route', token=token, _external=True)}'''
    mail.send(msg)

@app.route('/reset', methods=['GET', 'POST'])
def password_reset_route():
    if current_user.is_authenticated:
        return redirect(url_for('home_route'))
    form = PasswordReset()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        send_reset_email(user)
        return redirect(url_for('home_route'))
    return render_template('passwordreset.html', form=form)

@app.route('/new_password/<token>', methods=['GET', 'POST'])
def new_password_route(token):
    if current_user.is_authenticated:
        return redirect(url_for('home_route'))
    user = User.verify_reset_token(token)
    if user is None:
        return redirect(url_for('password_reset_route'))
    form = NewPassword()
    if form.validate_on_submit():
        pass_hash = bcrypt.generate_password_hash(form.password.data)
        user.password = pass_hash
        db.session.commit()
        return redirect(url_for('home_route'))
    return render_template('newpassword.html', form=form)
