import Bot
import math
class TrackingBot(Bot.Bot):
	def __init__(self, xposition, yposition, idnumber):
		Bot.Bot.__init__(self, xposition, yposition, 1, 1, "t", idnumber)
		self.status = "nPath"
		self.PotentialDrills = []
		self.PotentialStations = []
		self.EndFlag = 0
		
	def CreatePath(self, xstart, xfinish, shape): #this creates a full path
		direction = 1
		trackwidth = math.trunc(2*Bot.Bot.DetectionRange/3) #this makes sure we cover everything
		currentx = xstart+trackwidth #intial positions
		currenty = trackwidth
		shapexlen = len(shape) #store lengths of shape
		shapeylen = len(shape[0])
		while currentx < xfinish : #loop to find all points to track
			if direction == 1: #loop when going up
				currenty = trackwidth
				while currenty < shapeylen - self.ysize/2: #this loops from 0 to the top with protection from going over the border
					if shape[currentx][currenty] and shape[currentx][int(round(currenty + self.ysize/2))]: #checkss if position and bot are still in shape and appends to path
						self.Path.append([currentx, currenty])
					elif shape[currentx][currenty]: #if position is in shape but body would go over shape take a point before and append it to path
						self.Path.append([currentx ,(currenty - self.ysize/2)])
					currenty += 2*trackwidth
				
			else:
				currenty = shapeylen - trackwidth -1
				while currenty > self.ysize/2: #this loops from top to 0 and applies same logic
					if shape[currentx][currenty] and shape[currentx][int(round(currenty - self.ysize/2))]:
						self.Path.append([currentx, currenty])
					elif shape[currentx][currenty]:
						self.Path.append([currentx, currenty + self.ysize/2])
					currenty -= 2*trackwidth
					
			currenty = int(round(((shapeylen + direction*shapeylen)/2) - direction*trackwidth)) #resets currenty to 0 if direction was -1 and to shapeylen if direction was 1
			direction = -direction #switches direction
			if currentx + 2*trackwidth < (shapexlen-1) - self.xsize/2: #progresses currentx to the right, protecting from going outta bounds at the far right
				currentx = int(round(2*trackwidth + currentx))
			elif currentx == int(round((shapexlen - 1) - self.xsize/2)):
				currentx = xfinish			
			else:
				currentx = int(round((shapexlen - 1) - self.xsize/2))
				
		self.status = "Tracking"
	
	def Update(self, landfill, dt):
		if self.status == "Tracking":
			if len(self.Path) == 0:
				self.EndFlag = 1
				self.status = "SearchStation"
			else:
				self.UpdatePosition(dt)
				self.VerifyPockets(landfill)
				self.CheckObstacle(landfill.Obstacles)
				if (self.charge < 20) and (self.status != "FindDrill"):
					self.status = "SearchStation"
					landfill.TransmitSignal(["StationRequest" , [self.id]])
			
		
		if self.status == "GoStation":
			self.UpdatePosition(dt)
			if (abs(self.StationPosition[0]- self.xposition) < 1) and (abs(self.StationPosition[1] - self.yposition) < 1):
				self.status = "Charging"
			self.CheckObstacle(landfill.Obstacles)
		
		if self.status == "FindDrill":
			self.ChooseDrill(landfill)
			
		if self.status == "SearchStation":
			self.ChooseChargingStation(landfill)
						
		if self.status == "Charging":
			self.charge = min(100, self.charge + 3 * self.DischargeSpeed * dt)
			if self.charge == 100 and self.EndFlag == 0:
				self.status = "Tracking"
				landfill.TransmitSignal(["FreeStation", [self.StationId]])
				self.StationId = 0
			
	def VerifyPockets(self, landfill):
		for Pocket in landfill.GasPockets:
			if (math.sqrt((self.xposition - Pocket[0])**2+(self.yposition - Pocket[1])**2) < Bot.Bot.DetectionRange - 1):
				self.status = "FindDrill"
				landfill.TransmitSignal(["DrillingRequest" , [self.id]])
			
	def ReceiveSignal(self, signal, landfill):
		#signal is ["Signal Type" , [Content]]
		if (signal[0] == "DrillingAvailability") and (signal[1][0] == self.id):
			#For request signals, [Content] is [idumberOfRequester]
			self.PotentialDrills.append([signal[1][1], signal[1][2], signal[1][3]])

		elif (signal[0] == "StationAvailability") and (signal[1][0] == self.id):
			self.PotentialStations.append([signal[1][1], signal[1][2], signal[1][3]])
			
		elif (signal[0] == "FreeTBot") and (signal[1][0] == self.id):
			print("Hello")
			self.status = "Tracking"
	
	def ChooseDrill(self, landfill):
		if len(self.PotentialDrills) > 0:
			self.status = "WaitDrill"
			ClosestDrill = self.PotentialDrills[0]
			for Drill in self.PotentialDrills:
				if ((self.xposition - Drill[1])**2+(self.yposition - Drill[2])**2 < (self.xposition - ClosestDrill[1])**2+(self.yposition - ClosestDrill[2])**2):
					ClosestDrill = Drill
			landfill.TransmitSignal(["DrillSelection", [ClosestDrill[0], self.id, self.xposition, self.yposition]])
			self.PotentialDrills = []
		else :
			landfill.TransmitSignal(["DrillingRequest" , [self.id]])

		
	
