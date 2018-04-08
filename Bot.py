import math
import Entity
class Bot(Entity.Entity):
	
	Speed = 50
	DetectionRange = 5
	def __init__(self, xposition, yposition, xsize, ysize, symbol, idnumber):
		Entity.Entity.__init__(self, [xposition, yposition, xsize, ysize], symbol, idnumber)
		self.charge = 100
		self.TargetPosition = []
		self.Path = []
		self.DischargeSpeed = Bot.Speed/180
		self.Status = "pending"
		
	def UpdatePosition(self, dt): #Add checks
		dTargetx = self.Path[0][0] - self.xposition
		dTargety = self.Path[0][1] - self.yposition
		vx = Bot.Speed*dTargetx/math.sqrt(dTargetx**2+dTargety**2)
		vy = Bot.Speed*dTargety/math.sqrt(dTargetx**2+dTargety**2)
		self.xposition += vx*dt
		self.yposition += vy*dt
		self.charge -= self.DischargeSpeed * dt
		if (abs(self.Path[0][0] - self.xposition) < 0.5) and (abs(self.Path[0][1] - self.yposition) < 0.5):
			self.Path.remove(self.Path[0])
			
	def ChooseChargingStation(self, landfill):
		if len(self.PotentialStations) > 0:
			self.status = "GoStation"
			ClosestStation = self.PotentialStations[0]
			for Station in self.PotentialStations:
				if (math.sqrt((self.xposition - Station[1])**2+(self.yposition - Station[2])**2) < math.sqrt((self.xposition - ClosestStation[1])**2+(self.yposition - ClosestStation[2])**2)):
					ClosestStation = Station
			landfill.TransmitSignal(["StationSelection", [ClosestStation[0]]])
			self.StationPosition = [ClosestStation[1], ClosestStation[2]]
			self.Path.insert(0 , [ClosestStation[1], ClosestStation[2]])
			self.PotentialStations = []
			self.StationId = ClosestStation[0]
		else :
			landfill.TransmitSignal(["StationRequest" , [self.id]])
		
	def CheckObstacle(self, Obstacles):
		if len(self.Path) > 0:
			dTargetx = self.Path[0][0] - self.xposition
			dTargety = self.Path[0][1] - self.yposition
			dx = 0.5*dTargetx/math.sqrt(dTargetx**2+dTargety**2)
			dy = 0.5*dTargety/math.sqrt(dTargetx**2+dTargety**2)
			CheckPoint = [self.xposition, self.yposition]
			CheckPointList = [[CheckPoint[0], CheckPoint[1]]]
			for i in range(3):
				CheckPoint[0] += dx
				CheckPoint[1] += dy
				CheckPointList.append([CheckPoint[0], CheckPoint[1]])
			for Point in CheckPointList:
				for Obstacle in Obstacles:
					if ((abs(Point[0]-Obstacle.xposition) < ((self.xsize + Obstacle.xsize)/2 + 1)) and (abs(Point[1]-Obstacle.yposition) < ((self.ysize + Obstacle.ysize)/2 + 1))):
						self.AvoidObstacle(Obstacle)
					
	def AvoidObstacle(self, Obstacle):
		while((abs(self.Path[0][0]-Obstacle.xposition) < ((self.xsize + Obstacle.xsize)/2 +2)) and (abs(self.Path[0][1]-Obstacle.yposition) < ((self.ysize + Obstacle.ysize)/2 + 2))):
			self.Path.remove(self.Path[0])
		if (self.Path[0][0] > self.xposition):
			if (self.Path[0][1] > self.yposition):
				self.Path.insert(0, [Obstacle.xposition + ((self.xsize + Obstacle.xsize)/2 +2), Obstacle.yposition + ((self.ysize + Obstacle.ysize)/2 +2)])
				if ((self.xposition - (Obstacle.xposition - Obstacle.xsize)) > (self.yposition - (Obstacle.yposition - Obstacle.ysize))):
					self.Path.insert(0, [Obstacle.xposition + ((self.xsize + Obstacle.xsize)/2 +2), Obstacle.yposition - ((self.ysize + Obstacle.ysize)/2 +2)])
				else : self.Path.insert(0, [Obstacle.xposition - ((self.xsize + Obstacle.xsize)/2 +2), Obstacle.yposition + ((self.ysize + Obstacle.ysize)/2 +2)])
			else :
				self.Path.insert(0, [Obstacle.xposition + ((self.xsize + Obstacle.xsize)/2 +2), Obstacle.yposition - ((self.ysize + Obstacle.ysize)/2 +2)])
				if ((self.xposition - (Obstacle.xposition - Obstacle.xsize)) > ((Obstacle.yposition + Obstacle.ysize) - self.yposition)):
					self.Path.insert(0, [Obstacle.xposition + ((self.xsize + Obstacle.xsize)/2 +2), Obstacle.yposition + ((self.ysize + Obstacle.ysize)/2 +2)])
				else : self.Path.insert(0, [Obstacle.xposition - ((self.xsize + Obstacle.xsize)/2 +2), Obstacle.yposition - ((self.ysize + Obstacle.ysize)/2 +2)])
		else:
			if (self.Path[0][1] > self.yposition):
				self.Path.insert(0, [Obstacle.xposition - ((self.xsize + Obstacle.xsize)/2 +2), Obstacle.yposition + ((self.ysize + Obstacle.ysize)/2 +2)])
				if (((Obstacle.xposition + Obstacle.xsize) - self.xposition) > (self.yposition - (Obstacle.yposition - Obstacle.ysize))):
					self.Path.insert(0, [Obstacle.xposition - ((self.xsize + Obstacle.xsize)/2 +2), Obstacle.yposition - ((self.ysize + Obstacle.ysize)/2 +2)])
				else : self.Path.insert(0, [Obstacle.xposition + ((self.xsize + Obstacle.xsize)/2 +2), Obstacle.yposition + ((self.ysize + Obstacle.ysize)/2 +2)])
			else :
				self.Path.insert(0, [Obstacle.xposition - ((self.xsize + Obstacle.xsize)/2 +2), Obstacle.yposition - ((self.ysize + Obstacle.ysize)/2 +2)])
				if (((Obstacle.xposition + Obstacle.xsize) - self.xposition) > ((Obstacle.yposition + Obstacle.ysize) - self.yposition)):
					self.Path.insert(0, [Obstacle.xposition - ((self.xsize + Obstacle.xsize)/2 +2), Obstacle.yposition + ((self.ysize + Obstacle.ysize)/2 +2)])
				else : self.Path.insert(0, [Obstacle.xposition + ((self.xsize + Obstacle.xsize)/2 +2), Obstacle.yposition - ((self.ysize + Obstacle.ysize)/2 +2)])
				
