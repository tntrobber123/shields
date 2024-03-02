import pygame

from window import Window
window = Window()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.x = 300
        self.y = 300
        self.direction = 0
        self.image = pygame.image.load("test.png")
        
    def move_x(self, amnt):
    	self.x += amnt
    	
    def move_y(self, amnt):
    	self.y += amnt
    	
    def draw(self):
    	window.screen.blit(self.image, (self.x, self.y))
