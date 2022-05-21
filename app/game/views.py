from app.game import game
from app import db


# review the stat result
@game.route('/stat')
def stat():
	print('show stat')
	return None

# start the game, load text
@game.route('/start')
def start():
	print('game start')
	return None
	