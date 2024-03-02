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
		self.dist_x = self.mid_x - math.fabs(self.mouse_x)
		self.dist_y = self.mid_y - math.fabs(self.mouse_y)
		
		print(self.dist_x)
		
		#print(self.dist_y/self.dist_x)
		
		if self.dist_x == 0:
			self.dist_x = 1
			
		angle = -math.degrees(math.atan(self.dist_y/self.dist_x))
		self.new_image = pygame.transform.rotate(self.image, angle)
		print(angle)
		
	
	def draw(self):
		window.screen.blit(self.new_image, (self.x, self.y))
		window.screen.blit(self.new_image, (self.mid_x, self.mid_y))
		
	

