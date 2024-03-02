import pygame

from window import Window
window = Window()

class Level():
	def __init__(self):
		self.level_x = [400, 450]
		self.level_y = [400, 450]
		self.brick = pygame.image.load("sprites/bricks.png")
		
	def build(self):
		x = len(self.level_x)
		while x != 0:
			window.screen.blit(self.brick, (self.level_x[x - 1], self.level_y[x - 1]))
			x -= 1
