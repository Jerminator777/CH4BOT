import math
import Entity
import TrackingBot
import ChargingStation
import DrillingBot
class Landfill:
	def __init__(self, TBots, DBots, CStations, Pockets, Obstacles, Outline):
		self.xmax = Outline[0][0]
		self.xmin = Outline[0][0]
		self.ymax = Outline[0][1]
		self.ymin = Outline[0][1]
		for corner in Outline:
			self.xmax = max(self.xmax, corner[0])
			self.xmin = min(self.xmin, corner[0])
			self.ymax = max(self.ymax, corner[1])
			self.ymin = min(self.ymin, corner[1])
		self.xmax = self.xmax - self.xmin
		self.ymax = self.ymax - self.ymin
		self.createShape(Outline)
		self.TrackingBots = []
		for position in TBots:
			self.TrackingBots.append(TrackingBot.TrackingBot(position[0]-self.xmin, position[1]-self.ymin))
		self.Obstacles = []
		for block in Obstacles:
			self.Obstacles.append(Entity.Entity([block[0]-self.xmin, block[1]-self.ymin, block[2], block[3]], "x"))
		self.DrillingBots = []
		for position in DBots:
			self.DrillingBots.append(DrillingBot.DrillingBot(position[0]-self.xmin, position[1]-self.ymin))
		self.ChargingStations = []
		for position in CStations:
			self.ChargingStations.append(ChargingStation.ChargingStation(position[0]-self.xmin, position[1]-self.ymin))
		self.GasPockets = Pockets
		for pocket in self.GasPockets:
			pocket[0]-=self.xmin
			pocket[1]-=self.ymin
	def createShape(self, Outline):
		self.shape = [[0 for col in range(self.ymax+1)] for row in range(self.xmax+1)]
		for i in range(len(Outline)):
			self.shape[Outline[i][0]-self.xmin][Outline[i][1]-self.ymin] = 1;
			if i != 0:
				x = Outline[i][0]-self.xmin
				Dx = PreviousCorner[0]-Outline[i][0]
				y = Outline[i][1]-self.ymin
				Dy = PreviousCorner[1]-Outline[i][1]
				if (math.fabs(Dx) > math.fabs(Dy)):
					dx = math.fabs(Dx)/Dx+0.00001
					dy = Dy/math.fabs(Dx)+0.00001
					y += 0.5
					n = math.fabs(Dx)
				else:
					dx = Dx/math.fabs(Dy)+0.00001
					dy = math.fabs(Dy)/Dy+0.00001
					x += 0.5
					n = math.fabs(Dy)
				for j in range(math.trunc(n+0.5)):
					x += dx
					y += dy
					self.shape[math.trunc(x)][math.trunc(y)]=1
			PreviousCorner = Outline[i]
		x = Outline[0][0]-self.xmin
		Dx = PreviousCorner[0]-Outline[0][0]
		y = Outline[0][1]-self.ymin
		Dy = PreviousCorner[1]-Outline[0][1]
		if (math.fabs(Dx) > math.fabs(Dy)):
			dx = math.fabs(Dx)/Dx+0.00001
			dy = Dy/math.fabs(Dx)+0.00001
			y += 0.5
			n = math.fabs(Dx)
		else:
			dx = Dx/math.fabs(Dy)+0.00001
			dy = math.fabs(Dy)/Dy+0.00001
			x += 0.5
			n = math.fabs(Dy)
		for j in range(math.trunc(n+0.5)):
			x += dx
			y += dy
			self.shape[math.trunc(x)][math.trunc(y)]=1
		for i in range(len(self.shape)):
			for j in range(len(self.shape[i])):
				right = False
				left = False
				up = False
				down = False
				for k in range(len(self.shape)-i):
					if (self.shape[i+k][j] == 1):
						right = True
						break
				for k in range(i):
					if (self.shape[k][j] == 1):
						left = True
						break
				for k in range(len(self.shape[i])-j):
					if (self.shape[i][j+k] == 1):
						up = True
						break
				for k in range(j):
					if (self.shape[i][k] == 1):
						down = True
						break	
				if (right and left and down and up):
					self.shape[i][j]=1
		
		

