import pygame

import math

from window import Window
window = Window()

class Shield(pygame.sprite.Sprite):
	def __init__(self):
		self.x = 700
		self.y = 330
		self.mid_x = 645
		self.mid_y = 350
		self.image = pygame.image.load("sprites/pot_lid_side.png")
		
	def mouse(self):
		self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
		self.dist_x = (math.fabs(self.mouse_x-645))
		self.dist_y = (math.fabs(self.mouse_y-350))
		print(self.dist_x)
		print(self.dist_y)
		
		angle = math.tan(self.dist_y/self.dist_x)
		self.new_image = pygame.transform.rotate(self.image, angle)
		
	
	def draw(self):
		window.screen.blit(self.new_image, (self.x, self.y))
		window.screen.blit(self.new_image, (self.mid_x, self.mid_y))
		
	

