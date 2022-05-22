from flask import request, jsonify
from flask_login import login_required, current_user

from app.game import game
from app import db
from app.models import User, Stat


# review the stat result
@game.route('/stat', methods=['POST','GET'])
@login_required
def stat():
	if request.method == 'GET':
		print(current_user.Username)
		list_stat = Stat.query.filter_by(user = current_user.Username).all()
		# if history stat exists
		if list_stat:
			total_mistake = 0
			total_wpm = 0
			total_cpm = 0
			for s in list_stat:
				total_mistake += s.MIS
				total_wpm += s.WPM
				total_cpm += s.CPM

			return jsonify({
				'success':'',
				'average_mistake': total_mistake/len(list_stat),
				'average_cpm': total_cpm/len(list_stat),
				'average_wpm': total_wpm/len(list_stat),
				})
		# if history not exsiting
		else:
			print('no record')
			return jsonify({'error': 'No record, Please try for first time!'})

# start the game, load text
@game.route('/start')
def start():
	print('game start')
	return None
	