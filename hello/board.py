class Board:
	code1_path = "/app/hello/submissions/player1.txt"
	code2_path = "/app/hello/submissions/player2.txt"
	
	def set(self, player, code):
		if player == 1:
			path = self.code1_path
		else:
			path = self.code2_path
		
		text_file = open(path, "w")
		text_file.write(code)
		text_file.close()

	def get(self, player):
		if player == 1:
			path = self.code1_path
		else:
			path = self.code2_path
		return open (path, "r").read()


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
