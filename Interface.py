import matplotlib.pyplot as plt
import numpy
import pygame


#SECTION FOR TURNING LANDFILL MATRIX INTO .PNG FILE TO BE USED AS BACKGROUND OF PYTHON WINDOW
WINDOW
#Assuming landfill "map" comes in lists of binary lists
landfill_temp = [[0,0,0,0,0,0,0,0,0],
		[0,0,1,1,1,0,1,1,0],
		[0,0,1,1,1,1,1,1,0],
		[0,0,0,0,0,0,1,1,0],
		[0,0,0,0,0,0,0,0,0]]
landfill_size = [len(landfill_temp),len(landfill_temp[0])]
				 
#invert colours (black=1,white=0)
landfill_invert	= numpy.logical_not(landfill_temp).astype(int)

#save image. small white border remains.
fig = plt.imshow(landfill_invert, cmap='Greys')
plt.axis('off')
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)
plt.savefig('LandfillMap.png',bbox_inches='tight')


#SECTION FOR CREATING PYTHON WINDOW
#the landfill shape is turned into black and white .png and used as background image of window
#initializing window screen, screen background, and refresh time
clock = pygame.time.Clock()
background = pygame.image.load("LandfillMap.png")
background_size = background.get_rect().size
screen = pygame.display.set_mode(background_size)
pygame.display.set_caption("Simulation Window")

#loop for refreshing window
while True:	
	clock.tick(10) #controls how fast screen updates
	screen.blit(background, (0,0))
	pygame.display.flip()
