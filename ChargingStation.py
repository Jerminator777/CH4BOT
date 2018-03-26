import Entity
class ChargingStation(Entity.Entity):
	def __init__(self, xposition, yposition):
		Entity.Entity.__init__(self, [xposition, yposition, 25, 25], "c")
		self.status = "Available"
