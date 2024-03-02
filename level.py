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
        
        self.background = pygame.image.load("sprites/background.png")
        self.bricks = pygame.image.load("sprites/bricks.png")

        self.level_x = [500, 500, 500]
        self.level_y = [500, 600, 700]

    def draw(self):
        window.screen.blit(self.background, (self.x, self.y))

        for x, y in zip(self.level_x, self.level_y):
            window.screen.blit(self.bricks, (x, y))
    
    def update(self):
        print(self.world_shiftx)
        self.x += self.world_shiftx
        self.y += self.world_shifty
