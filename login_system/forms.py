from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from login_system.models import User

class RegistrationForm(FlaskForm):
    name = StringField('Full Name', validators=[DataRequired(), Length(min=4, max=50, message="Enter minimum 4 and maximum 50 characters.")])
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20, message="Enter minimum 4 and maximum 20 characters.")])
    email = EmailField('Email', validators=[DataRequired(), Email(message="Please enter valid e-mail address.")])
    password = PasswordField('Password', validators=[DataRequired()])
    pass_validate = PasswordField('Please enter your password again', validators=[DataRequired(), EqualTo('password', message="Password doesn't match.")])
    submit = SubmitField()

    def validate_field(self, field):
        if True:
            raise ValidationError('Something')

    def validate_username(self, username):
        user = User.query.filter_by(username = username.data).first()
        if user:
            raise ValidationError('Username not available, please choose another username.')

    def validate_email(self, email):
        user = User.query.filter_by(email = email.data).first()
        if user:
            raise ValidationError('Email not available, please choose another email.')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20, message="Enter minimum 4 and maximum 20 characters.")])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField()
