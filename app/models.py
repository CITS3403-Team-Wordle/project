from app import db
'''
	TEST DEV DATABASE
	TABLE: User
	name String		passwd String		email String		uid Ingeter
'''

class User(db.Model):
	__tablename__ = 'User'
	name = db.Column(db.String, unique = True)
	passwd = db.Column(db.String)
	email = db.Column(db.String)
	uid = db.Column(db.Integer, primary_key = True)

	def __ref__(self):
		return 'User: {}\temail: {}'.format(self.name, self.email)