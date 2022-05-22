from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo, ValidationError

from flask_wtf import FlaskForm
from wtforms import Form

from app.models import User

class loginForm(FlaskForm):
    Email = StringField('Email', [DataRequired(message = 'Email is required.'), Length(min=1, max=64), Email()])
    Password = StringField('Password', [DataRequired(message = 'Password is required.')])
    Remember_me = BooleanField('Remember me')


class signupForm(FlaskForm):
    # Username 'Username must have only letters, numbers ot underscores, with length min 6 and max 30'
    Username = StringField('Username', [DataRequired(message = 'Username is required.'), Length(min=6,max=30), Regexp('^[a-zA-Z][a-zA-Z0-9_]*$',0, 'Username must have only letters, numbers or underscores.')])

    # Password 'Password must have length min 6 and max 30, no other specifical rules'
    Password = StringField('Password', [DataRequired(message = 'Password is required.'), Length(min=8, max=30), EqualTo('Password_confirm', message='Passwords must match.')])
    Password_confirm = StringField('Password_confirm')

    # Email ''
    Email = StringField('Email', [DataRequired(message = 'Email is required.'), Length(min=1, max=64), Email()])
    Submit = SubmitField('Submit')
    
    def validate_Username(self, Username):
        if User.query.filter_by(Username = Username.data).first():
            raise ValidationError('Username already exists.')

    def validate_Email(self, Email):
        if User.query.filter_by(Email = Email.data).first():
            raise ValidationError('Email already exists.')




class forgetpasswordForm(FlaskForm):
    Password = StringField('Password', [DataRequired(message = 'Password is required.'), EqualTo('Password_confirm', message='Passwords must match.')])
    Password_confirm = StringField('Password_confirm')
    Submit = SubmitField('Submit')
    
class forgetpasswordForm_withName(forgetpasswordForm):
    Username = StringField('Username', [DataRequired(message = 'Username is required')])

    def validate_Username(self, Username):
        if not User.query.filter_by(Username = Username.data).first():
            raise ValidationError('Username not exists.')

class forgetpasswordForm_withEmail(forgetpasswordForm):
    Email = StringField('Email', [DataRequired(message = 'Email is required.'), Email()])

    def validate_Email(self, Email):
        if not User.query.filter_by(Email = Email.data).first():
            raise ValidationError('Email not exists.')
    
