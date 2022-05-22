import os

from app import create_app, db
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

app = create_app(os.environ.get('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
	return print(dict(app=app, db=db))

@manager.command
def test():
	'''To run unit_test'''
	import unittest
	test = unittest.TestLoader().discover('test')
	unittest.TextTestRunner(verbosity=2).run(test)

@manager.command
def deploy():
	""" Run deployment tasks """
	from flask_migrate import upgrade
	from app.models import User, Role, Text

	# migrate db to latest version
	upgrade()

	# add other code later...



manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__=='__main__':
	manager.run()
