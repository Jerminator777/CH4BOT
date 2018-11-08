import time



class Robots:
	MessageDict = {		#Content Format
	'Set Pos' 	: 0,	#[float x, float y]
	'Command' 	: 1,	#'String'
	'Set Path'	: 2, 	#[[x1, y1], [x2, y2], ... [xi, yi]]	
	'Pocket'	: 3		#[float x, float y]
	}
	DetectionRange = 2
	xsize = 1
	ysize = 1
	def __init__(self, ip, ix, iy, Type):
		self.Type = Type
		self.Charge = 100
		self.ip = ip
		self.x = ix
		self.y = iy
		self.status = 'pending'
		self.MessageBuffer = [[Robots.MessageDict['Set Pos'], [ix, iy]]]
		
	def setPosition(self, x, y):
		self.x = x
		self.y = y
		
	def setStatus(self, status):
		self.status = status[0]
		self.charge = status[1]
		
	def addMessage(self, message):
		self.MessageBuffer.append(message)
		
	def clearBuffer(self):
		self.MessageBuffer = []
