from werkzeug.security import generate_password_hash, check_password_hash
from flask import current_app

from flask_login import UserMixin

from app import db
from app import login_manager
'''
	TEST DEV DATABASE
	TABLE: User
	name String		passwd String		email String		uid Ingeter
'''

@login_manager.user_loader
def load_user(uid):
	return User.query.get(int(uid))

class User(UserMixin, db.Model):
	__tablename__ = 'Users'

	id = db.Column('id',db.Integer, primary_key = True)
	Username = db.Column(db.String(64), unique = True)
	Password_hash = db.Column(db.String(128))
	Email = db.Column(db.String(64), unique = True)
	#role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

	def __ref__(self):
		return 'User: {}\temail: {}'.format(self.name, self.email)

	# generate password hash
	def password_hash(self, password):
		self.Password_hash = generate_password_hash(password)

	# verify password
	def verify_password(self, password):
		return check_password_hash(self.Password_hash, password)