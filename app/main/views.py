from flask import render_template, session, redirect, url_for
from flask import request, jsonify
from app.main import main 

@main.route('/', methods=['POST', 'GET'])
def index():
	return render_template('index.html')
