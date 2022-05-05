from __init__ import db
'''
	TEST DEV DATABASE
	TABLE: User
	name varchar		passwd varchar		email varchar		uid ingeter
'''

class User(db.Model):
	__tablename__ = 'User'
	name = db.Column(db.String, unique = True)
	passwd = db.Column(db.String)
	email = db.Column(db.String)
	uid = db.Column(db.Integer, primary_key = True)

	def __ref__(self):
		return 'User: {}\temail: {}'.format(self.name, self.email)