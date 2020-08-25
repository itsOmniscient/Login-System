from flask import Flask, render_template, url_for, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '65d716bc87f6e63d1c2ad0953a77056d'

@app.route('/')
@app.route('/home')
def home_route():
    return render_template('index.html')

@app.route('/register', methods=('GET', 'POST'))
def register_route():
    form = RegistrationForm()
    if form.validate_on_submit():
        return redirect(url_for('home_route'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login_route():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('home_route'))
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
