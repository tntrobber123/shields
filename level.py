import pygame

from window import Window
window = Window()

class Level:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.height = 0
        self.bricks = pygame.image.load("sprites/bricks.png")
        self.background = pygame.image.load("sprites/background.png")
		
        self.blocks_x = [200, 300, 400]
        self.blocks_y = [300, 300, 300]
		
        self.move = "null"
        self.amount = 0
        self.collide = False

    def update(self):
        if self.move != "null":
            if self.move == "left":
                self.x += self.amount
            elif self.move == "right":
                self.x -= self.amount

        if self.amount >= 5:
            self.amount = 5

        window.screen.blit(self.background, (self.x, self.y))

    def jump(self):
        if self.collide:
            self.amount = 5
            self.move = "up"

    def gravity(self):
        if not self.collide:
            self.y += 0.25

    def collision(self, player_rect):
        for i in self.blocks_x:
            level_rect = pygame.Rect(self.blocks_x[i - 1], self.blocks_y[i - 1], self.blocks.get_width(), self.blocks.get_height())

            if level_rect.colliderect(player_rect):
                self.collide = True
            else:
                self.collide = False

