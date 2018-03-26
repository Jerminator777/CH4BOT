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
	def UpdatePosition(self, dt):
		dTargetx = self.Path[0] - self.xposition
		dTargety = self.Path[1] - self.yposition
		vx = Bot.Speed*dTargetx/math.sqrt(dTargetx**2+dTargety**2)
		vy = Bot.Speed*dTargety/math.sqrt(dTargetx**2+dTargety**2)
		self.xposition += vx*dt
		self.yposition += vy*dt
		self.charge -= self.DischargeSpeed * dt
		

