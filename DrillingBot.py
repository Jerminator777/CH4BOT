import Bot
class DrillingBot(Bot.Bot):
	def __init__(self, xposition, yposition, idnumber):
		Bot.Bot.__init__(self, xposition, yposition, 20, 20, "d", idnumber)
		self.status = "SearchStation"
		self.DischargeSpeed = Bot.Bot.Speed/900
		
	def SendAvailability(self, landfill, signal):
	if self.status == "Available":
		landfill.TransmitSignal(["DrillingAvailability" , [signal[1][0], self.id, self.xposition, self.yposition]])
	
	def ReceiveSignal(self, signal, landfill):
		#signal is ["Signal Type" , [Content]]
		if signal[0] == "DrillingRequest":
			#For request signals, [Content] is [idnumberOfRequester]
			self.SendAvailability(landfill, signal)
		elif (signal[0] == "DrillSelection") and (signal[1][0] == self.id):
			self.status = "Journey"
			Path.insert(0, [signal[1][1], signal[1][2]])
		elif (signal[0] == "StationAvailability") and (signal[1][0] == self.id):
			self.PotentialStations.append([signal[1][1], signal[1][2], signal[1][3]])

