import Bot
import math
class DrillingBot(Bot.Bot):
	def __init__(self, xposition, yposition, idnumber):
		Bot.Bot.__init__(self, xposition, yposition, 2, 2, "d", idnumber)
		self.status = "SearchStation"
		self.DischargeSpeed = Bot.Bot.Speed/90
		self.PotentialStations = []
		
	def Update(self, landfill, dt):
		if self.status == "PocketRemoval":
			self.UpdatePosition(dt)
			for Pocket in landfill.GasPockets:
				if (math.sqrt((self.xposition - Pocket[0])**2+(self.yposition - Pocket[1])**2) < Bot.Bot.DetectionRange +2):
					landfill.GasPockets.remove(Pocket)
					self.status = "SearchStation"
					landfill.TransmitSignal(["FreeTBot", [self.RequesterId]])
					print (["FreeTBot", [self.RequesterId]])
					break
			
		if self.status == "Journey":
			self.UpdatePosition(dt)
			self.CheckObstacle(landfill.Obstacles)
			if (abs(self.RequesterPosition[0] - self.xposition) < 25) and (abs(self.RequesterPosition[1] - self.yposition) < 25):
				self.status = "PocketRemoval"
				
		if self.status == "GoStation":
			self.UpdatePosition(dt)
			if (abs(self.StationPosition[0]- self.xposition) < 1) and (abs(self.StationPosition[1] - self.yposition) < 1):
				self.status = "Charging"
			self.CheckObstacle(landfill.Obstacles)
			
		if self.status == "SearchStation":
			self.ChooseChargingStation(landfill)
						
		if self.status == "Charging":
			self.charge = min(100, self.charge + 3 * self.DischargeSpeed * dt)
			if self.charge == 100 :
				self.status = "Available"
		
	def SendAvailability(self, landfill, signal):
		if ((self.status == "Available") or (((self.status == "Charging") or (self.status == "GoStation")) and (self.charge > 50))):
			landfill.TransmitSignal(["DrillingAvailability" , [signal[1][0], self.id, self.xposition, self.yposition]])
	
	def ReceiveSignal(self, signal, landfill):
		#signal is ["Signal Type" , [Content]]
		if signal[0] == "DrillingRequest":
			#For request signals, [Content] is [idnumberOfRequester]
			self.SendAvailability(landfill, signal)
			
		elif (signal[0] == "DrillSelection") and (signal[1][0] == self.id):
			self.status = "Journey"
			self.Path = [[signal[1][2], signal[1][3]]]
			self.RequesterId = signal[1][1]
			self.RequesterPosition = [signal[1][2], signal[1][3]]
			landfill.TransmitSignal(["FreeStation", [self.StationId]])
			self.StationId = 0
			
		elif (signal[0] == "StationAvailability") and (signal[1][0] == self.id):
			self.PotentialStations.append([signal[1][1], signal[1][2], signal[1][3]])

