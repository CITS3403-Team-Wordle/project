from werkzeug.security import generate_password_hash, check_password_hash
from flask import current_app

from flask_login import UserMixin
from hashlib import md5
from datetime import datetime, timedelta, date

from app import db
from app import login_manager


@login_manager.user_loader
def load_user(uid):
	return User.query.get(int(uid))


#==========	Table Role ==========
class Role(db.Model):
	__tablename__ = 'Role'
	id = db.Column(db.Integer, primary_key=True)
	role = db.Column(db.String(64), unique=True)

	users = db.relationship('User', backref='Role', lazy=True)

	def __ref__(self):
		return 'Role {}'.format(self.role)


#==========	Table User ==========
class User(UserMixin, db.Model):
	__tablename__ = 'User'

	id = db.Column('id',db.Integer, primary_key = True)
	Username = db.Column(db.String(64), unique = True)
	Password_hash = db.Column(db.String(128))
	Email = db.Column(db.String(64), unique = True)

	role_id = db.Column(db.Integer, db.ForeignKey('Role.id'))

	stat = db.relationship('Stat', backref='User', lazy=True)
	token = db.relationship('Token', backref='User', lazy=True)

	def __ref__(self):
		return 'User: {}\temail: {}'.format(self.Username, self.Email)

	# generate password hash
	def password_hash(self, password):
		self.Password_hash = generate_password_hash(password)

	# verify password
	def verify_password(self, password):
		return check_password_hash(self.Password_hash, password)

	def generate_token(self):
		token = datetime.utcnow()
		
		return token

	def revoke_token(self):
		pass


	def verify_token(self, token):

		return False
		


#==========	Table Token ==========
class Token(db.Model):
	__tablename__ = 'Token'
	id =  db.Column(db.Integer, primary_key=True)
	token_expiration = db.Column(db.DateTime)

	user_id = db.Column(db.Integer, db.ForeignKey('User.id'))

	def __ref__(self):
		return 'user_id: {}\ttoken: {}'.format(self.user_id, self.token)


#========== Table Text ==========
class Text(db.Model):
	__tablename__ = 'Text'
	id = db.Column(db.Integer, primary_key=True)
	text = db.Column(db.String)

	def __ref__(self):
		return 'Text: {}'.format(self.text)

#========== Table Stat ==========
class Stat(db.Model):
	__tablename__ = 'Stat'
	id = db.Column(db.Integer, primary_key=True)
	CPM = db.Column(db.Integer)
	WPM = db.Column(db.Integer)
	date = db.Column(db.String)
	user = db.Column(db.String, db.ForeignKey('User.Username'))

	def __ref__(self):
		return 'CPM: {}\tWPM: {}\tdate: {}'.format(self.CPM, self.WPM, self.date)

	