import math
class Landfill:
	def __init__(self, TBots, DBots, CStations, Pockets, Obstacles, Outline):
		self.xmax = 0
		self.xmin = 0
		self.ymax = 0
		self.ymin = 0
		for corner in Outline:
			self.xmax = max(self.xmax, corner[0])
			self.xmin = min(self.xmin, corner[0])
			self.ymax = max(self.ymax, corner[1])
			self.ymin = min(self.ymin, corner[1])
		self.xmax = self.xmax - self.xmin
		self.ymax = self.ymax - self.ymin
		self.shape = [[0 for col in range(self.ymax+1)] for row in range(self.xmax+1)]
		for i in range(len(Outline)):
			self.shape[Outline[i][0]-self.xmin][Outline[i][1]-self.ymin] = 1;
			if i != 0:
				x = Outline[i][0]-self.xmin
				Dx = PreviousCorner[0]-Outline[i][0]
				y = Outline[i][1]-self.ymin
				Dy = PreviousCorner[1]-Outline[i][1]
				if (math.fabs(Dx) > math.fabs(Dy)):
					dx = math.fabs(Dx)/Dx
					dy = Dy/math.fabs(Dx)
					n = math.fabs(Dx)
				else:
					dx = Dx/math.fabs(Dy)
					dy = math.fabs(Dy)/Dy
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
			dx = math.fabs(Dx)/Dx
			dy = Dy/math.fabs(Dx)
			n = math.fabs(Dx)
		else:
			dx = Dx/math.fabs(Dy)
			dy = math.fabs(Dy)/Dy
			n = math.fabs(Dy)
		for j in range(math.trunc(n+0.5)):
			x += dx
			y += dy
			self.shape[math.trunc(x)][math.trunc(y)]=1
		self.TrackingBots = []
		for position in TBots:
			self.TrackingBots.append(Tracking_Bot(position[0]-self.xmin, position[1]-self.ymin))
		self.DrillingBots = []
		for position in DBots:
			self.DrillingBots.append(Drilling_Bot(position[0]-self.xmin, position[1]-self.ymin))
		self.ChargingStations = []
		for position in CStations:
			self.ChargingStations.append(Charging_Station(position[0]-self.xmin, position[1]-self.ymin))
		self.GasPockets = Pockets
		for pocket in self.GasPockets:
			pocket[0]-=self.xmin
			pocket[1]-=self.ymin

