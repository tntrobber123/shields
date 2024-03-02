import pygame

from window import Window
window = Window()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.x = 300
        self.y = 300
        self.direction = 0
        self.move = "null"
        self.amount = 0
        self.image = pygame.image.load("sprites/bricks.png")
        
    def movement(self):
    	if self.move == "up":
    		self.y -= self.amount
    	elif self.move == "down":
    		self.y += self.amount
    	elif self.move == "left":
    		self.x -= self.amount
    	elif self.move == "right":
    		self.x += self.amount
    		
    def draw(self):
    	window.screen.blit(self.image, (self.x, self.y))
