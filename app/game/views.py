from flask import request, jsonify
from flask_login import login_required

from app.game import game
from app import db


# review the stat result
@game.route('/stat', methods=['POST','GET'])
@login_required
def stat():
	if request.method == 'GET':
		print('show stat')
	return jsonify({'success': 'hello stat'})

# start the game, load text
@game.route('/start')
def start():
	print('game start')
	return None
	