import pygame

from window import Window
window = Window()

class Level(pygame.sprite.Sprite):
    def __init__(self):
        self.platform_list = pygame.sprite.Group()
        self.world_shiftx = 0
        self.world_shifty = 0
        self.x = 0
        self.y = 0
        
        self.background = pygame.image.load("sprites/dark_bricks.png")
        self.bricks = pygame.image.load("sprites/bricks.png")

        self.level_x = [500, 500, 500]
        self.level_y = [500, 600, 700]

    def draw(self):
        a = 50
        b = 0
        while a != 0:
            c = 20
            d = 0
            while c != 0:
                window.screen.blit(self.background, (self.x + b, self.y + d))
                c -= 1
                d += 50
                
            a -= 1
            b += 50
            
        a = len(self.level_x)
        while a > 0:
            self.level_x[a - 1] += self.world_shiftx
            self.level_y[a - 1] += self.world_shifty
            a -= 1

        for x, y in zip(self.level_x, self.level_y):
            window.screen.blit(self.bricks, (x, y))
    
    def update(self):
        self.x += self.world_shiftx
        self.y += self.world_shifty
