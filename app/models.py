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

	@staticmethod
	def insert_roles():
		roles = ['admin', 'user']
		for r in roles:
			temp_role = Role.query.filter_by(role=r).first()
			if not temp_role:
				temp_role = Role(role=r)
			db.session.add(temp_role)
		db.session.commit()


#==========	Table User ==========
class User(UserMixin, db.Model):
	__tablename__ = 'User'

	id = db.Column('id',db.Integer, primary_key = True)
	Username = db.Column(db.String(64), unique = True)
	Password_hash = db.Column(db.String(128))
	Email = db.Column(db.String(64), unique = True)

	role_id = db.Column(db.Integer, db.ForeignKey('Role.id'))

	stat = db.relationship('Stat', backref='User', lazy=True)

	def __ref__(self):
		return 'User: {}\temail: {}'.format(self.Username, self.Email)

	@staticmethod
	def insert_users():
		# insert default Administrator
		admin = User(Username='Administrator', Email='admin@email.com', Role=Role.query.filter_by(role='admin').first())
		# default password for Admin 'cits3403'
		admin.password_hash('cits3403')
		db.session.add(admin)
		db.session.commit()

	# generate password hash
	def password_hash(self, password):
		self.Password_hash = generate_password_hash(password)

	# verify password
	def verify_password(self, password):
		return check_password_hash(self.Password_hash, password)


#========== Table Text ==========
class Text(db.Model):
	__tablename__ = 'Text'
	id = db.Column(db.Integer, primary_key=True)
	text = db.Column(db.String)

	def __ref__(self):
		return 'Text: {}'.format(self.text)

	@staticmethod
	def insert_texts():
		f = open('app/game_text_example.txt', 'r')
		for p in f.readlines():
			db.session.add(Text(text=p))
		db.session.commit()
		f.close()


#========== Table Stat ==========
class Stat(db.Model):
	__tablename__ = 'Stat'
	id = db.Column(db.Integer, primary_key=True)
	MIS = db.Column(db.Integer)
	CPM = db.Column(db.Integer)
	WPM = db.Column(db.Integer)
	date = db.Column(db.DateTime)
	user = db.Column(db.String, db.ForeignKey('User.Username'))

	def __ref__(self):
		return 'CPM: {}\tWPM: {}\tdate: {}'.format(self.CPM, self.WPM, self.date)

	