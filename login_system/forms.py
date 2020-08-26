from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    name = StringField('Full Name', validators=[DataRequired(), Length(min=4, max=50, message="Enter minimum 4 and maximum 50 characters.")])
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20, message="Enter minimum 4 and maximum 20 characters.")])
    email = EmailField('Email', validators=[DataRequired(), Email(message="Please enter valid e-mail address.")])
    password = PasswordField('Password', validators=[DataRequired()])
    pass_validate = PasswordField('Please enter your password again', validators=[DataRequired(), EqualTo('password', message="Password doesn't match.")])
    submit = SubmitField()

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20, message="Enter minimum 4 and maximum 20 characters.")])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField()
