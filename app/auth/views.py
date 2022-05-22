from flask import render_template, session, redirect, url_for, request, jsonify
import wtforms_json
from flask_login import login_user, logout_user, login_required
from werkzeug.urls import url_parse


#import os

from app.auth.forms import signupForm, loginForm, forgetpasswordForm_withName, forgetpasswordForm_withEmail
from app.auth import auth
from app import db
from app.models import User

@auth.route('/login', methods=['POST'])
def login():
	#print('start login')
	json = request.get_json()
	form = loginForm(
		Email = json['Email'],
		Password = json['Password'],
		Remember_me = json['Remember_me']
	)
	# temprarily skip the csrf_token validation
	if form.validate_on_submit() or (len(form.errors)==1 and 'csrf_token' in form.errors):
		user = User.query.filter_by(Email = form.Email.data).first()
		#print(user)

		if user and user.verify_password(form.Password.data):
			login_user(user, remember=form.Remember_me.data)
			next_page = request.args.get('next')
			if not next_page or url_parse(next_page).netloc != '':
				next_page = '/'
			return jsonify({ 'success': 'logged in'})
		return jsonify({ 'error': 'bad user' })
	else:
			return jsonify({ 'error': 'bad user' })

@auth.route('/signup', methods=['POST'])
def signup():
	json = request.get_json()
	form = signupForm(
		Username=json['Username'],
		Password = json['Password'],
		Password_confirm = json['Password_confirm'],
		Email = json['Email']
		)

	# temprarily skip the csrf_token validation
	if form.validate_on_submit() or (len(form.errors)==1 and 'csrf_token' in form.errors):
		user = User(Username=form.Username.data, Email=form.Email.data)
		user.password_hash(form.Password.data)
		db.session.add(user)
		db.session.commit()

		#token = user.generate_confirm_token()

		return jsonify({ 'success': 'signed in' })
	else:
		error_msg = ''
		for e in form.errors:
			error_msg += form.errors[e][0]+'\n'
			#print(form.errors[e])
		return jsonify({'error': error_msg})


@auth.route('/logout')
@login_required
def logout():
	logout_user()
	print('user logout')
	return jsonify({'success': 'logged out'})


@auth.route('/forgetpassword', methods=['POST'])
def forgetpassword():
	json = request.get_json()

	print(json)

	# test whether Username or Email is choosen
	if '@' in json['identity']:
		print('Have Email')
		form = forgetpasswordForm_withEmail(
				Email = json['identity'],
				Password = json['new_password'],
				Password_confirm = json['confirm_new_password'],
			)
	else:
		print('Have Username')
		form = forgetpasswordForm_withName(
				Username = json['identity'],
				Password = json['new_password'],
				Password_confirm = json['confirm_new_password'],
			)
	
	if form.validate_on_submit() or (len(form.errors)==1 and 'csrf_token' in form.errors):
		if form.Username:
			User.query.filter(User.Username == form.Username).update({ 'Password_hash': generate_password_hash(form.Password) }, synchronize_session="fetch")



	return jsonify({'error': 'just connected!'})


'''
This route only for testing herf link
'''
@auth.route('/forgetpassword', methods=['GET'])
def show_forgetpassword():
	return render_template('auth/forgetpassword.html')

