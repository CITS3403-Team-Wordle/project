from wtforms import StringField, PasswordField, SubmitField
from wtforms import validators
from flask_wtf import FlaskForm

class LoginForm(FlaskForm):
    name = StringField('Username', [validators.DataRequired()])
    passwd = StringField('Password', [validators.DataRequired()])
    email = StringField('Email', [validators.DataRequired()])
    submit = SubmitField('Submit')