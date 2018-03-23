import Bot
class TrackingBot:
	def __init__(self, xposition, yposition):
		Bot.Bot.__init__(self, xposition, yposition, 10, 10, "t")
		self.status = "nPath"
