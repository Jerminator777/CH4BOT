import math
import Entity
class Bot(Entity.Entity):
	
	Speed = 10
	def __init__(self, xposition, yposition, xsize, ysize, symbol, idnumber):
		Entity.Entity.__init__(self, [xposition, yposition, xsize, ysize], symbol, idnumber)
		self.charge = 100
		self.TargetPosition = []
		self.Path = []
		self.DischargeSpeed = Bot.Speed/1800
		self.Status = "pending"
		
	def UpdatePosition(self, dt): #Add checks
		if(self.Status != "Charging") and (self.Status != "WaitDrill")
			dTargetx = self.Path[0][0] - self.xposition
			dTargety = self.Path[0][1] - self.yposition
			vx = Bot.Speed*dTargetx/math.sqrt(dTargetx**2+dTargety**2)
			vy = Bot.Speed*dTargety/math.sqrt(dTargetx**2+dTargety**2)
			self.xposition += vx*dt
			self.yposition += vy*dt
			self.charge -= self.DischargeSpeed * dt
			
	def ChooseChargingStation(self, landfill):
		self.status = "Station"
		ClosestStation = self.PotentialStations[0]
		for Station in self.PotentialStations:
			if (math.sqrt((self.xposition - Station[1])**2+(self.xposition - Station[2])**2) < math.sqrt((self.xposition - ClosestStation[1])**2+(self.xposition - ClosestStation[2])**2):
				ClosestStation = Station
		landfill.TransmitSignal(["StationSelection", [ClosestStation[0]]])
		self.Path.insert(0 , [ClosestStation[1], ClosestStation[2]])
		self.PotentialStations = []
		
	def CheckObstacle(self, Obstacles):
		dTargetx = self.Path[0][0] - self.xposition
		dTargety = self.Path[0][1] - self.yposition
		dx = 5*dTargetx/math.sqrt(dTargetx**2+dTargety**2)
		dy = 5*dTargety/math.sqrt(dTargetx**2+dTargety**2)
		CheckPoint = [self.xposition + self.xsize/2 , self.yposition + self.ysize/2]
		CheckPointList = [Checkpoint]
		for i in range(6):
			CheckPoint[0] += dx
			CheckPoint[1] += dy
			CheckPointList.append(CheckPoint)
		for Point in CheckPointList:
			for Obstacle in Obstacles:
				if ((abs(Point[0]-Obstacle.xposition) < ((self.xsize + Obstacle.xsize)/2 + 5)) and (abs(Point[1]-Obstacle.yposition) < ((self.ysize + Obstacle.ysize)/2 + 5))):
					self.AvoidObstacle(Obstacle)
					
	def AvoidObstacle(self, Obstacle):
		while((abs(Path[0][0]-Obstacle.xposition) < ((self.xsize + Obstacle.xsize)/2 +5)) and (abs(Path[0][1]-Obstacle.yposition) < ((self.ysize + Obstacle.ysize)/2 + 5))):
			self.Path.remove(Path[0])
		if (Path[0][0] > self.xposition):
			if (Path[0][1] > self.yposition):
				self.Path.insert(0, [Obstacle.xposition + ((self.xsize + Obstacle.xsize)/2 +5), Obstacle.yposition + ((self.ysize + Obstacle.ysize)/2 +5)])
				if ((self.xposition - (Obstacle.xposition - Obstacle.xsize)) > (self.yposition - (Obstacle.yposition - Obstacle.ysize))):
					self.Path.insert(0, [Obstacle.xposition + ((self.xsize + Obstacle.xsize)/2 +5), Obstacle.yposition - ((self.ysize + Obstacle.ysize)/2 +5)])
				else : self.Path.insert(0, [Obstacle.xposition - ((self.xsize + Obstacle.xsize)/2 +5), Obstacle.yposition + ((self.ysize + Obstacle.ysize)/2 +5)])
			else :
				self.Path.insert(0, [Obstacle.xposition + ((self.xsize + Obstacle.xsize)/2 +5), Obstacle.yposition - ((self.ysize + Obstacle.ysize)/2 +5)])
				if ((self.xposition - (Obstacle.xposition - Obstacle.xsize)) > ((Obstacle.yposition + Obstacle.ysize) - self.yposition)):
					self.Path.insert(0, [Obstacle.xposition + ((self.xsize + Obstacle.xsize)/2 +5), Obstacle.yposition + ((self.ysize + Obstacle.ysize)/2 +5)])
				else : self.Path.insert(0, [Obstacle.xposition - ((self.xsize + Obstacle.xsize)/2 +5), Obstacle.yposition - ((self.ysize + Obstacle.ysize)/2 +5)])
		else:
			if (Path[0][1] > self.yposition):
				self.Path.insert(0, [Obstacle.xposition - ((self.xsize + Obstacle.xsize)/2 +5), Obstacle.yposition + ((self.ysize + Obstacle.ysize)/2 +5)])
				if (((Obstacle.xposition + Obstacle.xsize) - self.xposition) > (self.yposition - (Obstacle.yposition - Obstacle.ysize))):
					self.Path.insert(0, [Obstacle.xposition - ((self.xsize + Obstacle.xsize)/2 +5), Obstacle.yposition - ((self.ysize + Obstacle.ysize)/2 +5)])
				else : self.Path.insert(0, [Obstacle.xposition + ((self.xsize + Obstacle.xsize)/2 +5), Obstacle.yposition + ((self.ysize + Obstacle.ysize)/2 +5)])
			else :
				self.Path.insert(0, [Obstacle.xposition - ((self.xsize + Obstacle.xsize)/2 +5), Obstacle.yposition - ((self.ysize + Obstacle.ysize)/2 +5)])
				if (((Obstacle.xposition + Obstacle.xsize) - self.xposition) > ((Obstacle.yposition + Obstacle.ysize) - self.yposition)):
					self.Path.insert(0, [Obstacle.xposition - ((self.xsize + Obstacle.xsize)/2 +5), Obstacle.yposition + ((self.ysize + Obstacle.ysize)/2 +5)])
				else : self.Path.insert(0, [Obstacle.xposition + ((self.xsize + Obstacle.xsize)/2 +5), Obstacle.yposition - ((self.ysize + Obstacle.ysize)/2 +5)])
				
