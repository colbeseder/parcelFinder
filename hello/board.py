class Board:
	code1_path = "/app/hello/submissions/player1.txt"
	code2_path = "/app/hello/submissions/player1.txt"
	
	def set(self, player, code):
		if player == 1:
			pass
		else:
			pass

	def get(self, player):
		if player == 1:
			return open (self.code1_path, "r").read()
		else:
			return open (self.code2_path, "r").read()
			
	

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
