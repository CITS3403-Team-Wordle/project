from flask import render_template, session, redirect, url_for
from . import main 

@main.route('/index', methods=['POST', 'GET'])
def index():
	return render_template('index.html')
