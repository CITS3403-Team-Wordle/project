from flask import render_template, session, redirect, url_for
from flask import request, jsonify
from app.main import main 

@main.route('/', methods=['POST', 'GET'])
def homepage():
	return render_template('main.html')


'''
@main.route('/signup', methods=['POST'])
def signup():

	json = request.get_json()
	print(json)
	if json['email'] and json['password']:
		return jsonify({'success': 'logged in'})
	else:
		return jsonify({'error': "bad data"})
'''