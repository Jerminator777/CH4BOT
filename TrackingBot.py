import Bot
import math
class TrackingBot(Bot.Bot):
	def __init__(self, xposition, yposition, idnumber):
		Bot.Bot.__init__(self, xposition, yposition, 10, 10, "t", idnumber)
		self.status = "nPath"
		self.PotentialDrills = []
		self.PotentialStations = []
		
		def CreatePath(self, xstart, xfinish, shape, coverage): #this creates a full path
		direction = 1
		trackwidth = math.floor(2*coverage/3) #this makes sure we cover everything
		currentx = xstart+trackwidth #intial positions
		currenty = trackwidth
		shapexlen = len(shape) #store lengths of shape
		shapeylen = len(shape[0])
		while currentx < xfinish: #loop to find all points to track
			if direction == 1: #loop when going up
				while currenty < shapeylen - self.ysize/2: #this loops from 0 to the top with protection from going over the border
					if shape[currentx,currenty] and shape[currentx,currenty + self.ysize/2]: #checkss if position and bot are still in shape and appends to path
						self.path.append([currentx,currenty])
					elif shape[currentx,currenty]: #if position is in shape but body would go over shape take a point before and append it to path
						self.path.append([currentx,currenty - self.ysize/2])
					currenty += 2*trackwidth
			else:
				while currenty => 0 + self.ysize/2: #this loops from top to 0 and applies same logic
					if shape[currentx,currenty] and shape[currentx,currenty - self.ysize/2]:
						self.path.append([currentx,currenty])
					elif shape[currentx,currenty]:
						self.path.append([currentx,currenty + self.size/2])
					currenty -= 2*trackwidth
					
			currenty = ((shapeylen + direction*shapeylen)/2) - direction*trackwidth #resets currenty to 0 if direction was -1 and to shapeylen if direction was 1
			directiom *= -1 #switches direction
			if currentx + 2*trackwidth < (shapexlen-1) - self.xsize/2: #progresses currentx to the right, protecting from going outta bounds at the far right
				currentx += 2*trackwidth
			else:
				currentx = (shapexlen - 1) - self.xsize/2
				
		def ReceiveSignal(self, signal, landfill):
			#signal is ["Signal Type" , [Content]]
			if (signal[0] == "DrillingAvailability") and (signal[1][0] == self.id):
				#For request signals, [Content] is [idumberOfRequester]
				self.PotentialDrills.append([signal[1][1], signal[1][2], signal[1][3]])

			elif (signal[0] == "StationAvailability") and (signal[1][0] == self.id):
				self.PotentialStations.append([signal[1][1], signal[1][2], signal[1][3]])

		def ChooseDrill(self, landfill):
			self.status = "WaitDrill"
			ClosestDrill = self.PotentialStations[0]
			for Drill in self.PotentialDrills:
				if (math.sqrt((self.xposition - Drill[1])**2+(self.xposition - Drill[2])**2) < math.sqrt((self.xposition - ClosestDrill[1])**2+(self.xposition - DrillStation[2])**2):
					ClosestDrill = Drill
			landfill.TransmitSignal(["StationSelection", [ClosestDrill[0], self.xposition, self.yposition]])
			sself.PotentialDrill = []
			
		
