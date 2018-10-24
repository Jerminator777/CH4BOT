import time

class Robots():
	def __init__(self, ip):
		self.ip = ip
		self.x = 0
		self.y = 0
		
	def sendPickle(self, message):
		self.x = self.x
		
	def setPosition(self, x, y):
		self.sendPickle("blablaxy")
		self.x = x
		self.y = y
	
