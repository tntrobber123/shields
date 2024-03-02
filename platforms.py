import pygame
import sys

class Platform(pygame.sprite.Sprite):
    def __init__(self):
        self.brick = pygame.image.load("sprites/bricks.png")
        self.brick = self.brick.get_rect()
