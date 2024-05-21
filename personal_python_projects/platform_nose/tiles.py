import pygame 

class Tile(pygame.sprite.Sprite):
	def __init__(self,pos,size):
		super().__init__()
		self.image = pygame.Surface((size,size))# x and y # create sq surface
		self.image.fill('grey')
		self.rect = self.image.get_rect(topleft = pos) #set the position of the square

	def update(self,x_shift):
		self.rect.x += x_shift