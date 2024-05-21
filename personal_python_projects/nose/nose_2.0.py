import pygame
from pygame.locals import * 
import random

pygame.init()

# conf screen
width, height = 1600, 900
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("The Nose")

#define game variables
#tile_size = 50

# images

nose_img = pygame.image.load('img/nose.png')
kovalev_img = pygame.image.load('img/kovalev.png')
bg_img = pygame.image.load('img/sp_nose.png')

#def draw_grid():
	#for line in range(0, 20):
		#pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (screen_width, line * tile_size))
		#pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_height))

#class World():
    #def __init__(sel,data):
        

# main loop

runn = True
while runn:
    
    screen.blit(bg_img, (0, 0))
    screen.blit(nose_img, (600, 600))
    screen.blit(kovalev_img, (400, 400))
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runn = False
    
    pygame.display.update()        

# end pygame
pygame.quit()