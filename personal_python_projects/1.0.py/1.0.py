import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('The Nose')
clock = pygame.time.Clock()

#test_surface = pygame.Surface((100,200)) #3 x and y
test_surface = pygame.image.load('')
test_surface.fill('Red')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
   
    screen.blit(test_surface, (200,100))         
    screen.blit(test_surface, (200,100))
            
    # draw elements
    # update everything
    pygame.display.update()
    clock.tick(60)