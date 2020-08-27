import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('CSRFSK')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/loginsystem.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from login_system import routes
