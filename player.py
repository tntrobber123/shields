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
        self.speed = 3

        self.direction = "D"
        self.image = pygame.image.load('sprites/player.png')
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y

        self.handle_collision()

        self.rect.y += self.change_y
        self.steps += self.change_steps

        self.handle_collision()
        
        if self.direction == "R":
            self.image = pygame.image.load('sprites/player.png')
            level.world_shiftx = 3
        
        if self.direction == "L":
            self.image = pygame.image.load('sprites/player_left.png')
            level.world_shiftx = -3
        
    def handle_collision(self):
        # Handling x-axis collisions
        self.rect.x += self.change_x
        
        a = 0
        while a > 0:
            block_hit_list_x = pygame.sprite.collide_rect(self, level.level_x[a - 1])
            for block in block_hit_list_x:
                if self.change_x > 0:
                    self.rect.right = block.rect.left
                elif self.change_x < 0:
                    self.rect.left = block.rect.right

            block_hit_list_y = pygame.sprite.collide_rect(self, level.level_y[a - 1])
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
            a -= 1

    def move(self, direction):
        if direction == "L":
            self.rect.x += self.change_x
            self.rect.y += self.change_y
            self.image = pygame.image.load('sprites/player_left.png')
            self.update_level()
            level.world_shiftx = 3
        elif direction == "R":
            self.rect.x += self.change_x
            self.rect.y += self.change_y
            self.image = pygame.image.load('sprites/player.png')
            self.update_level()
            level.world_shiftx = -3
        elif direction == "U":
            self.rect.x += self.change_x
            self.rect.y += self.change_y
            self.update_level()
            level.world_shifty = -3
        elif direction == "D":
            self.rect.x += self.change_x
            self.rect.y += self.change_y
            level.world_shifty = -3
            self.update_level()
            
        self.change_steps = 1

        a = len(level.level_x)
        while a > 0:
            level.level_x[a - 1] += level.world_shiftx
            level.level_y[a - 1] += level.world_shifty
            a -= 1

    def update_level(self):
        a = len(level.level_x)
        while a > 0:
            level.level_x[a - 1] += level.world_shiftx
            level.level_y[a - 1] += level.world_shifty
            a -= 1

    def stop(self):
        self.change_x = 0
        self.change_y = 0
        self.change_steps = 0
        level.world_shiftx = 0
        level.world_shifty = 0
        self.direction = "O"
        
    def draw(self):
        window.screen.blit(self.image, (645 - 37, 300))
