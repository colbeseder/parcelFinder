class Fetch:
	example1 = "console.log('ex1<p>');"
	example2 = "console.log('ex2<p>');"
	def __init__(self, player):
		self.player = player
	
	def whoami(self):
		return self.player

	def mine(self, escape=True):
		return self.example1

	def theirs(self, escape=True):
		return self.example2
