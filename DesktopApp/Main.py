from tkinter import *
from GUI import *
from Server import *
from Robots import *
import imageio
import time
import numpy as np
from PIL import Image

#Section to modify later depending on what we choose for the input settings
#Set the shape of the area here

Shape =	[	[0		,	0],
			[800	,	0],
			[800	,	600],
			[0		,	500]]

Serv = Server('192.168.2.30', Shape)

while True:
	#Serv.CheckMessages() #Will not do anything without clients to interact with
	Serv.Interface.Wndw.update()
	Serv.Interface.Wndw.update_idletasks()
