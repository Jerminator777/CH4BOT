import Bot
class DrillingBot:
	def __init__(self, xposition, yposition):
		Bot.Bot.__init__(self, xposition, yposition, 20, 20, "d")
		self.status = "SearchStation"
