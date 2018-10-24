from tkinter import *
from GUI import *
from Server import *
from Robots import *
import imageio
import time
import numpy as np
from PIL import Image

#Section to modify later depending on what we choose for the input settings
text_file = open("./FieldParam.txt","r")		
lines = []		
for line in text_file:		
	coord = line.split()	
	if len(coord) == 3:	
		d = ""
		coord.append(d)
		coord.append(d)
	coord_tup = tuple(coord)	
	lines.append(coord_tup)	
text_file.close()		
FieldParam = {}		
for cat,x,y,dx,dy in lines:		
	int_x = int(x)	
	int_y = int(y)
	try:	
		int_dx=int(dx)
		int_dy=int(dy)
		co = [int_x,int_y,int_dx,int_dy]
	except ValueError:	
		co = [int_x,int_y]
	try:	
		FieldParam[cat].append(co)
	except KeyError:	
		FieldParam[cat]=[co]
#lf = Landfill.Landfill(FieldParam["track"], FieldParam["drill"], FieldParam["charge"], FieldParam["gas"], FieldParam["obstacle"], FieldParam["field"])
#Shape = lf.shape
#Shape = np.asarray(Shape)
#Shape = Shape.transpose()
#landfill_size = [len(Shape[0]),len(Shape)]  #[length,height]
#				 
##invert colours (black=1,white=0)
#imageio.imwrite('LandfillMap.png',(Shape))
##END of temp section

Interface = GUI()
Serv = Server('Salut')

while True:
	Serv.CheckMessages()
	Interface.Wndw.update()
	Interface.Wndw.update_idletasks()
