class Board:
	code1 = "console.log('ex1<p>');"
	code2 = "console.log('ex2<p>');"
	
	set(player, code):
		if player == 1:
			code1 = code
		else:
			code2 = code

class Fetch
	def __init__(self, board, player):
		self.board = board
		self.player = player
	
	def whoami(self):
		return self.player

	def mine(self):
		return board.code1

	def theirs(self):
		return board.code2