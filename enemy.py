import pygame

from window import Window
window = Window()

from level import Level
level = Level()

class Enemy(pygame.sprite.sprite)
	def __init__(self):
		self.image(pygame.image.load('sprites/bad_guy_.png')
