from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_route():
    return render_template('index.html')

@app.route('/register')
def register_route():
    return render_template('register.html')

@app.route('/login')
def login_route():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
