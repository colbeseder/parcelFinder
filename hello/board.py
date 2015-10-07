class Board:
	code1 = "console.log('ex1<p>');"
	code1_path = "console.log('ex1<p>');"
	code2 = "console.log('ex2<p>');"
	
	def set(self, player, code):
		if player == 1:
			code1 = code
		else:
			code2 = code
			
	def get(self, player):
		if player == 1:
			return open (code1_path, "r").read()
		else:
			return code2
			
	

class Fetch:
	def __init__(self, board, player):
		self.board = board
		self.player = player
	
	def whoami(self):
		return self.player
	
	def whoishe(self):
		if self.player == 1:
			return 2
		else:
			return 1

	def mine(self):
		return self.board.get(self.whoami())

	def theirs(self):
		return self.board.get(self.whoishe())
	
	def set_mine(self, code):
		self.board.set(self.player, code)
