import math
import Entity
class Bot(Entity.Entity):
	
	Speed = 10
	def __init__(self, xposition, yposition, xsize, ysize, symbol):
		Entity.Entity.__init__(self, [xposition, yposition, xsize, ysize], symbol)
		self.charge = 100
		self.TargetPosition = []
		self.Path = []
		self.DischargeSpeed = Bot.Speed/1800
		self.Status = "pending"
		
	def UpdatePosition(self, dt):
		if(self.Status != "Charging")
			dTargetx = self.Path[0][0] - self.xposition
			dTargety = self.Path[0][1] - self.yposition
			vx = Bot.Speed*dTargetx/math.sqrt(dTargetx**2+dTargety**2)
			vy = Bot.Speed*dTargety/math.sqrt(dTargetx**2+dTargety**2)
			self.xposition += vx*dt
			self.yposition += vy*dt
			self.charge -= self.DischargeSpeed * dt
		
	def CheckObstacle(self, Obstacles):
		dTargetx = self.Path[0][0] - self.xposition
		dTargety = self.Path[0][1] - self.yposition
		dx = -5*dTargetx/math.sqrt(dTargetx**2+dTargety**2)
		dy = -5*dTargety/math.sqrt(dTargetx**2+dTargety**2)
		CheckPoint = self.Path[0]
		CheckPointList = [Checkpoint]
		for i in range(math.trunc(math.sqrt(dTargetx**2+dTargety**2))):
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
				
