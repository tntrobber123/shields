import pygame

from window import Window
window = Window()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 645 - 32
        self.y = 295
        self.move = "null"
        self.image = pygame.image.load("sprites/player.png")
        self.rect = self.image.get_rect()

    def movement(self):
        if self.move == "left":
            self.image = pygame.image.load("sprites/player_left.png")
        elif self.move == "right":
            self.image = pygame.image.load("sprites/player.png")

    def draw(self):
        window.screen.blit(self.image, (self.x, self.y))
