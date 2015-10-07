class Board:
	code1 = "console.log('ex1<p>');"
	code2 = "console.log('ex2<p>');"
	
	def set(player, code):
		if player == 1:
			code1 = code
		else:
			code2 = code

class Fetch:
	def __init__(self, board, player):
		self.board = board
		self.player = player
	
	def whoami(self):
		return self.player

	def mine(self):
		return self.board.code1

	def theirs(self):
		return self.board.code2
	
	def set_mine(self, code):
		self.board.set(self.player, code)
