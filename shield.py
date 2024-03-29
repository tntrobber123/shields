import pygame
import math

from window import Window
window = Window()

from player import Player
player = Player()

from level import Level
level = Level()

class Shield(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 700
        self.y = 330
        self.mid_x = 645
        self.mid_y = 350
        self.angle = 0
        self.speed = False
        self.image = pygame.image.load("sprites/pot_lid_side.png")

    def mouse(self):
        self.x = 650
        self.y = 330
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        self.dist_x = self.mouse_x - self.mid_x
        self.dist_y = self.mouse_y - self.mid_y

        self.angle = -math.degrees(math.atan2(self.dist_y, self.dist_x)) + 90
        self.new_image = pygame.transform.rotate(self.image, self.angle)
    
        rect = self.new_image.get_rect(center=(self.x, self.y))
    
        self.x, self.y = rect.topleft

        angle_rad = math.radians(self.angle)
        self.x += 75 * math.sin(angle_rad)
        self.y += 75 * math.cos(angle_rad)

    def draw(self):
        window.screen.blit(self.new_image, (self.x, self.y))
