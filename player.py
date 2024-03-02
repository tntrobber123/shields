import pygame

from window import Window
window = Window()

from level import Level
level = Level()

#from constants import SCREEN_HEIGHT, SCREEN_WIDTH, PLAYER_SPEED

class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.change_x = 0
        self.change_y = 0
        self.steps = 0
        self.change_steps = 0

        self.direction = "D"
        self.level = None
        self.image = pygame.image.load('sprites/player.png')
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y

        self.handle_collision(self.level)

        self.rect.y += self.change_y
        self.steps += self.change_steps

        self.handle_collision_y()

        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height

    def handle_collision(self, level):
        # Handling x-axis collisions
        self.rect.x += self.change_x
        block_hit_list_x = pygame.sprite.spritecollide(self, level.level_x, False)
        for block in block_hit_list_x:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                self.rect.left = block.rect.right

        # Handling y-axis collisions
        self.rect.y += self.change_y
        block_hit_list_y = pygame.sprite.spritecollide(self, level.level_y, False)
        for block in block_hit_list_y:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

        # Resetting position after collision handling
        self.rect.x -= self.change_x
        self.rect.y -= self.change_y

        # Resetting change values after collision
        if block_hit_list_x or block_hit_list_y:
            self.change_x = 0
            self.change_y = 0


    def move(self, direction):
        if direction == "L":
            self.change_x = -PLAYER_SPEED
        elif direction == "R":
            self.change_x = PLAYER_SPEED
        elif direction == "U":
            self.change_y = -PLAYER_SPEED
        elif direction == "D":
            self.change_y = PLAYER_SPEED
        self.change_steps = 1
        self.direction = direction

    def stop(self):
        self.change_x = 0
        self.change_y = 0
        self.change_steps = 0
