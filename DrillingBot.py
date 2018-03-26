import Bot
class DrillingBot(Bot.Bot):
	def __init__(self, xposition, yposition):
		Bot.Bot.__init__(self, xposition, yposition, 20, 20, "d")
		self.status = "SearchStation"
		self.DischargeSpeed = Bot.Bot.Speed/900
