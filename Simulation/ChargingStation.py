import Entity
class ChargingStation(Entity.Entity):
	def __init__(self, xposition, yposition, idnumber):
		Entity.Entity.__init__(self, [xposition, yposition, 2.5, 2.5], "c", idnumber)
		self.status = "Available"
		
	def SendAvailability(self, landfill, signal):
		if self.status == "Available":
			landfill.TransmitSignal(["StationAvailability" , [signal[1][0], self.id, self.xposition, self.yposition]])
		
	def ReceiveSignal(self, signal, landfill):
		#signal is ["Signal Type" , [Content]]
		if signal[0] == "StationRequest":
			#For request signals, [Content] is [idumberOfRequester]
			self.SendAvailability(landfill, signal)
		elif (signal[0] == "StationSelection") and (signal[1][0] == self.id):
			self.status = "Reserved"
		elif (signal[0] == "FreeStation") and (signal[1][0] == self.id):
			self.status = "Available"
