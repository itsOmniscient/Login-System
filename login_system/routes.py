from login_system import app, db, bcrypt
from flask import Flask, render_template, url_for, redirect
from login_system.forms import RegistrationForm, LoginForm
from login_system.models import User

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
        return redirect(url_for('home_route'))
    return render_template('login.html', form=form)
