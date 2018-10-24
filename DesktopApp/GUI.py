from tkinter import *
import Robots
import Server
from PIL import Image
import imageio

class GUI():
	def __init__(self):
		self.Wndw = Tk()
		self.Wndw.title("CH4TBOT Monitoring Window")
		MainFrame = Frame(self.Wndw)
		MainFrame.pack(side = 'top')
		ButtonFrame = Frame(MainFrame)
		ButtonFrame.pack(side = 'right', padx = 50, pady = 50)
		
		PauseButton = Button(ButtonFrame, command = self.PauseProcess, text = 'Pause', width = 20)
		PauseButton.pack( side = 'top', pady = 10)
		
		StopButton = Button(ButtonFrame, command = self.StopProcess, text = 'Stop', width = 20)
		StopButton.pack( side = 'top', pady = 10)
		
		StartButton = Button(ButtonFrame, command = self.StartProcess, text = 'Start', width = 20)
		StartButton.pack( side = 'top', pady = 10)
		
		RecallButton = Button(ButtonFrame, command = self.RecallProcess, text = 'Recall', width = 20)
		RecallButton.pack( side = 'top', pady = 10)
		
		StatusFrame = Frame(MainFrame, width = 300, height = 600)
		StatusFrame.pack(side = 'right')
		
		TrackingStatusText = StringVar()
		TrackingStatusLabel = Label(StatusFrame, textvariable = TrackingStatusText)
		TrackingStatusText.set('What is love?')
		TrackingStatusLabel.place(x = 0, y = 0)
	
		MapFrame = Frame(MainFrame,width = 800, height = 600)
		MapFrame.pack(side = 'left')
		self.img = PhotoImage(file='LandfillMap.png')
		Mapbg = Label(MapFrame, image = self.img)
		Mapbg.place(x = 0, y = 0)
		
		Entities = {}
		TBotimg = PhotoImage(file='TrackingBot.png')
		DBotimg = PhotoImage(file='DrillingBot.png')
	
	def PauseProcess(self):
		print('poil')
	
	def StopProcess(self):
		print('poilu')
	
	def StartProcess(self):
		print('poils')
	
	def RecallProcess(self):
		print('toison')
	
