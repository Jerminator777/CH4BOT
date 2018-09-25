class Entity:
	def __init__(self, Coordinates, symbol, idnumber):
		self.symbol = symbol
		self.xposition = Coordinates[0]
		self.yposition = Coordinates[1]
		self.xsize = Coordinates[2]
		self.ysize = Coordinates[3]
		self.id = idnumber
