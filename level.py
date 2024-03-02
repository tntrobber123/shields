import pygame

from window import Window
window = Window()

class Level:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.bricks = pygame.image.load("sprites/bricks.png")
        self.background = pygame.image.load("sprites/background.png")

        self.move = "null"
        self.amount = 0
        
        
    def update(self):
        while self.move != "null":
            if self.move == "up":
                self.y -= self.amount
            elif self.move == "down":
                self.y += self.amount
            elif self.move == "left":
                self.x -= self.amount
            elif self.move == "right":
                self.x += self.amount
                
        window.screen.blit(self.background, (self.x, self.y))
