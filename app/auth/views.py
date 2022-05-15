from flask import render_template, session, redirect, url_for, request

#import os

from app.auth.forms import LoginForm
from app.auth import auth
from app import db
from app.models import User


@auth.route('/login', methods=['POST', 'GET'])
def login():
	form = LoginForm(request.form)
	name = None

	if form.validate_on_submit():
		usr = User(name=form.name.data, passwd=form.passwd.data, email=form.email.data)
		db.session.add(usr)
		db.session.commit()
		name = form.name.data
		return redirect('main')
	else:
		print(form.errors)

	return render_template('auth/login.html',form=form, name=name)

