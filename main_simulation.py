import imageio
import numpy as np
import pygame
import Landfill

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
lf = Landfill.Landfill(FieldParam["track"], FieldParam["drill"], FieldParam["charge"], FieldParam["gas"], FieldParam["obstacle"], FieldParam["field"])
Shape = lf.shape
Shape = np.asarray(Shape)
Shape = Shape.transpose()
landfill_size = [len(Shape[0]),len(Shape)]  #[length,height]
				 
#invert colours (black=1,white=0)
imageio.imwrite('LandfillMap.png',(Shape))

clock = pygame.time.Clock()
background = pygame.image.load("LandfillMap.png")
background_size = background.get_rect().size        #(length,height)
ratio = int(1000/background_size[1])
background = pygame.transform.scale(background, [ratio*background_size[0], ratio*background_size[1]])
background_size = background.get_rect().size        #(length,height)
screen = pygame.display.set_mode(background_size)
pygame.display.set_caption("Simulation Window")

#getting dimensions of one element in matrix using background image dimensions and binary matrix dimensions

#import charging station icon and re-size to meet background element ratio
StationIcon = pygame.image.load("ChargingStation.png")
PocketIcon = pygame.image.load("Pocket.png")
ObstacleIcon = pygame.image.load("obstacle.png")
TrackingIcon = pygame.image.load("TrackingBot.png")
DrillingIcon = pygame.image.load("DrillingBot.png")
#picture = pygame.transform.scale(picture, ratio)
while len(lf.GasPockets) > 0:#loop for refreshing window
	pygame.event.get()
	clock.tick() #controls how fast screen updates
	lf.UpdateBots(clock.get_time()/1000)
	screen.blit(background, (0,0))
	for station in lf.ChargingStations :
		screen.blit(StationIcon, (int(station.xposition * ratio-7), int(station.yposition * ratio-7)))
	for TBot in lf.TrackingBots :
		screen.blit(TrackingIcon, (int(TBot.xposition * ratio-7), int(TBot.yposition * ratio-7)))
	for DBot in lf.DrillingBots :
		screen.blit(DrillingIcon, (int(DBot.xposition * ratio-7), int(DBot.yposition * ratio-7)))
	for Obstacle in lf.Obstacles :
		screen.blit(pygame.transform.scale(ObstacleIcon, [Obstacle.xsize * ratio, Obstacle.ysize * ratio]), (int((Obstacle.xposition - Obstacle.xsize/2) * ratio), int((Obstacle.yposition - Obstacle.ysize/2) * ratio)))
	for Pocket in lf.GasPockets :
		screen.blit(PocketIcon, (int(Pocket[0] * ratio-7), int(Pocket[1] * ratio-7)))
	pygame.display.flip()
wait = input("PRESS ENTER TO CONTINUE.")


