import random
from flask import request, jsonify
from flask_login import login_required, current_user
from datetime import datetime, timedelta, date
from sqlalchemy import func

from app.game import game
from app import db
from app.models import User, Stat, Text


# store or review the stat result
@game.route('/stat', methods=['POST','GET'])
@login_required
def stat():
	# GET stat, showing results
	if request.method == 'GET':
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
				'average_mistake': round(total_mistake/len(list_stat),2),
				'average_cpm': round(total_cpm/len(list_stat),2),
				'average_wpm': round(total_wpm/len(list_stat),2),
				})
		# if history not exsiting
		else:
			return jsonify({'error': 'No record, Please try for first time!'})
	elif request.method == 'POST':
		json = request.get_json()
		stat = Stat(MIS=json['mistake'], WPM=json['wpm'], CPM=json['cpm'], date=datetime.now(), User=User.query.filter_by(Username=current_user.Username).first())
		db.session.add(stat)
		db.session.commit()
		return jsonify({'success': 'Uploaded grade!'})

# get text for typing game
@game.route('/game-text', methods=['GET'])
@login_required
def game_text():
	p_count = Text.query.count()
	if p_count:
		text = Text.query.filter_by(id=(int(p_count*random.random()+1))).first().text
		return jsonify({
			'success': '',
			'paragraph': text,
			})
	else:
		return jsonify({'error': 'empty Text'})






	