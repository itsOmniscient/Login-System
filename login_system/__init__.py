import os
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('CSRFSK')

from login_system import routes
