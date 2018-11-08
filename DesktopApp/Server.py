from tkinter import *
from GUI import *
from Robots import *
import math
import imageio
import time
import numpy as np
from PIL import Image
import pickle
import socket

class Server:
	MessageDict = {			#Content Format
	'Init' 			: 0	,	#
	'Pos Updt'		: 1	,	#[float x, float y]
	'Status Updt'	: 2	,	#['string', float charge]
	'Pocket'		: 3		#[float x, float y]
	}
	def __init__(self, ip, Outline):
		self.ip = ip
		self.CreateShape(Outline)
		self.Track = Robots('192.168.2.20', 0, 0, 'Tracking Robot')
		self.Track.addMessage([Robots.MessageDict['Set Path'], self.CreatePath()])
		self.Drill = Robots('192.168.2.40', 0, 0, 'Drilling Robot')
		self.Interface = GUI(self.Track.ip, self.Drill.ip, self)
		self.RobotList = {self.Track.ip : self.Track, self.Drill.ip : self.Drill}
		self.TCP_Port = 2009
		self.BufferSize = 2000 
		self.tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
		self.tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
		self.tcpServer.bind(('', self.TCP_Port))
		
	def CheckMessages(self):
		tcpServer.listen(4) 
		(conn, (ip,port)) = tcpServer.accept() 
		data = conn.recv(2048)
		data = pickle.loads(data)
		for message in data:
			if message[0] == Server.MessageDict['Init']:
				print('Connected to ' + ip)
				
			elif message[0] == Server.MessageDict['Pos Updt']:
				self.RobotList[ip].setPosition(message[1][0], message[1][1])
				GUI.UpdateRobotPos(RobotList[ip])
				
			elif message[0] == Server.MessageDict['Status Updt']:
				self.RobotList[ip].setStatus(message[1])
				GUI.UpdateRobotStatus(RobotList[ip])
				
			elif message[0] == Server.MessageDict['Pocket']:
				self.Drill.addMessage([Robots.MessageDict['Pocket'], message[1]])
				
			else: 
				print('Wrong Message Received')
	
		self.Interface.Wndw.update()
		self.Interface.Wndw.update_idletasks()
		conn.send(pickle.dumps(RobotList[ip].MessageBuffer))
		self.RobotList[ip].clearBuffer
		
	def CreateShape(self, Outline):
		xmax = Outline[0][0]
		xmin = Outline[0][0]
		ymax = Outline[0][1]
		ymin = Outline[0][1]
		
		for corner in Outline:
			xmax = max(xmax, corner[0])
			xmin = min(xmin, corner[0])
			ymax = max(ymax, corner[1])
			ymin = min(ymin, corner[1])
		xmax = xmax - xmin
		ymax = ymax - ymin
		self.shape = [[0 for col in range(ymax+1)] for row in range(xmax+1)]
		for i in range(len(Outline)):
			self.shape[Outline[i][0]-xmin][Outline[i][1]-ymin] = 1;
			x = Outline[i][0]-xmin
			Dx = Outline[i-1][0]-Outline[i][0]
			y = Outline[i][1]-ymin
			Dy = Outline[i-1][1]-Outline[i][1]
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
		Shape = np.asarray(self.shape)
		Shape = Shape.transpose()		 
		#invert colours (black=1,white=0)
		imageio.imwrite('LandfillMap.png',(Shape))
			
	def CreatePath(self):
		Path = []
		direction = 1
		trackwidth = math.trunc(2*Robots.DetectionRange/3) #this makes sure we cover everything
		currentx = trackwidth #intial positions
		currenty = trackwidth
		shapexlen = len(self.shape) #store lengths of shape
		shapeylen = len(self.shape[0])
		while currentx < shapexlen - Robots.xsize/2 : #loop to find all points to track
			if direction == 1: #loop when going up
				currenty = trackwidth
				while currenty < shapeylen - Robots.ysize/2: #this loops from 0 to the top with protection from going over the border
					if self.shape[currentx][currenty] and self.shape[currentx][int(round(currenty + Robots.ysize/2))]: #checkss if position and bot are still in shape and appends to path
						Path.append([currentx, currenty])
					elif self.shape[currentx][currenty]: #if position is in shape but body would go over shape take a point before and append it to path
						Path.append([currentx ,(currenty - Robots.ysize/2)])
					currenty += 2*trackwidth
				
			else:
				currenty = shapeylen - trackwidth - 1
				while currenty > Robots.ysize/2: #this loops from top to 0 and applies same logic
					if self.shape[currentx][currenty] and self.shape[currentx][int(round(currenty - Robots.ysize/2))]:
						Path.append([currentx, currenty])
					elif self.shape[currentx][currenty]:
						Path.append([currentx, currenty + Robots.ysize/2])
					currenty -= 2*trackwidth
			
			currenty = int(round(((shapeylen + direction*shapeylen)/2) - direction*trackwidth)) #resets currenty to 0 if direction was -1 and to shapeylen if direction was 1		
			direction = -direction #switches direction
			if currentx + 2*trackwidth < (shapexlen - 1) - Robots.xsize/2: #progresses currentx to the right, protecting from going out of bounds at the far right
				currentx = int(round(2*trackwidth + currentx))
			elif currentx == int(round((shapexlen - 1) - Robots.xsize/2)):
				currentx = shapexlen			
			else:
				currentx = int(round((shapexlen - 1) - Robots.xsize/2))
		
		return Path
			
