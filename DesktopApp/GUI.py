from tkinter import *
from PIL import Image
import imageio
import Robots

class GUI:
	def __init__(self, trackip, drillip, server):
		self.Wndw = Tk()
		self.Wndw.title('CH4TBOT Monitoring Window')
		MainFrame = Frame(self.Wndw)
		MainFrame.pack(side = 'top')
		ButtonFrame = Frame(MainFrame)
		ButtonFrame.pack(side = 'right', padx = 50, pady = 50)
		
		PauseButton = Button(ButtonFrame, command = lambda : self.PauseProcess(server), text = 'Pause', width = 20)
		PauseButton.pack( side = 'top', pady = 10)
		
		StopButton = Button(ButtonFrame, command = lambda: self.StopProcess(server), text = 'Stop', width = 20)
		StopButton.pack( side = 'top', pady = 10)
		
		StartButton = Button(ButtonFrame, command = lambda : self.StartProcess(server), text = 'Start', width = 20)
		StartButton.pack( side = 'top', pady = 10)
		
		RecallButton = Button(ButtonFrame, command = lambda : self.RecallProcess(server), text = 'Recall', width = 20)
		RecallButton.pack( side = 'top', pady = 10)
		
		StatusFrame = Frame(MainFrame, width = 300, height = 600)
		StatusFrame.pack(side = 'right')
		
		MapFrame = Frame(MainFrame,width = 800, height = 600)
		MapFrame.pack(side = 'left')
		self.img = PhotoImage(file='LandfillMap.png')
		Mapbg = Label(MapFrame, image = self.img)
		Mapbg.place(x = 0, y = 0)
		
		TBotimg = PhotoImage(file='TrackingBot.png')
		DBotimg = PhotoImage(file='DrillingBot.png')
		
		Entities = {trackip : Label(MapFrame, image = TBotimg), drillip : Label(MapFrame, image = DBotimg)}
		
		TrackStatus = StringVar()
		DrillStatus = StringVar()
		
		TrackingStatusLabel = Label(StatusFrame, textvariable = TrackStatus)
		TrackStatus.set('Tracking Robot Pending')
		TrackingStatusLabel.place(x = 0, y = 0)

		DrillingStatusLabel = Label(StatusFrame, textvariable = DrillStatus)
		DrillStatus.set('Drilling Robot Pending')
		DrillingStatusLabel.place(x = 0, y = 20)		
		
		Statuses = {trackip : TrackStatus, drillip : DrillStatus}
		
	def UpdateRobotPos(self, Robot):
		Entities[Robot.ip].place(x = Robot.x, y = Robot.y)
		
	def UpdateRobotStatus(self, Robot):
		Statuses[Robot.ip].set(Robot.Type + '\t' + string(Robot.Charge) + '%\t' + Robot.status)
		
	def PauseProcess(self, server):
		server.Track.addMessage([Server.MessageDict['Command'], 'Pause'])
		server.Drill.addMessage([Server.MessageDict['Command'], 'Pause'])
	
	def StopProcess(self, server):
		server.Track.addMessage([Server.MessageDict['Command'], 'Stop'])
		server.Drill.addMessage([Server.MessageDict['Command'], 'Stop'])
	
	def StartProcess(self, server):
		server.Track.addMessage([Server.MessageDict['Command'], 'Start'])
		server.Drill.addMessage([Server.MessageDict['Command'], 'Start'])
	
	def RecallProcess(self, server):
		server.Track.addMessage([Server.MessageDict['Command'], 'Recall'])
		server.Drill.addMessage([Server.MessageDict['Command'], 'Recall'])
	
