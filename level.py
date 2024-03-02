import pygame
from window import Window

class Level:
    def __init__(self):
        self.level_x = [600, 450]
        self.level_y = [400, 450]
        self.x = 0
        self.y = 0
        self.bricks = pygame.image.load("sprites/bricks.png")
        self.background = pygame.image.load("sprites/background.png")
        self.blocks = pygame.sprite.Group()

        for x, y in zip(self.level_x, self.level_y):
            block = pygame.sprite.Sprite()
            block.image = self.bricks
            block.rect = block.image.get_rect(topleft=(x, y))
            self.blocks.add(block)

        self.move = "null"
        self.amount = 0

    def build(self):
        self.blocks.draw(Window.screen)

    def movement(self, player):
        for block in self.blocks:
            if player.rect.colliderect(block.rect):
                print("Collision with block")

        for i in range(len(self.level_x)):
            if self.move == "up":
                self.level_y[i] -= self.amount
            elif self.move == "down":
                self.level_y[i] += self.amount
            elif self.move == "left":
                self.level_x[i] -= self.amount
            elif self.move == "right":
                self.level_x[i] += self.amount
                
        screen.blit(self.background, (self.x, self.y))

    def gravity(self):
        for i in range(len(self.level_y)):
            self.level_y[i] += 1
