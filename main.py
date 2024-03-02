import pygame
import random
import math

from window import Window
window = Window()

from player import Player
player = Player()

from level import Level
level = Level()

from shield import Shield
shield = Shield()

def main():
    
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    
    while True:
        
        for event in pygame.event.get():
            if event.type == exit:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    level.move = "up"
                    level.amount = 5
                    level.jump()
                elif event.key == pygame.K_a:
                    player.move = "left"
                    level.move = "left"
                    level.amount += 1
                elif event.key == pygame.K_d:
                    player.move = "right"
                    level.move = "right"
                    level.amount += 1
                	
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    level.amount -= 1
                elif event.key == pygame.K_a:
                    level.amount = 0
                elif event.key == pygame.K_d:
                	level.amount = 0
                
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
        
        player.movement()
        shield.mouse()

        window.screen.fill(BLACK)
        
        level.update()
        player.draw()
        shield.draw()
        
        pygame.display.flip()

main()
