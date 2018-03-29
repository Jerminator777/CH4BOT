import Bot
class TrackingBot(Bot.Bot):
	def __init__(self, xposition, yposition, idnumber):
		Bot.Bot.__init__(self, xposition, yposition, 10, 10, "t", idnumber)
		self.status = "nPath"
