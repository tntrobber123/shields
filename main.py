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
                    player.direction = ("U")
                    level.world_shifty = 3
                elif event.key == pygame.K_a:
                    player.direction = ("L")
                    level.world_shiftx = 3
                elif event.key == pygame.K_d:
                    player.direction = ("R")
                    level.world_shiftx = -3
                	
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    level.world_shiftx = 0
                    level.world_shifty = 0
                    player.stop()
                elif event.key == pygame.K_a:
                    level.world_shiftx = 0
                    level.world_shifty = 0
                    player.stop()
                elif event.key == pygame.K_d:
                    level.world_shiftx = 0
                    level.world_shifty = 0
                    player.stop()
                elif event.key == pygame.K_s:
                    level.world_shiftx = 0
                    level.world_shifty = 0
                    player.stop()
                	
                
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
        
        player.handle_collision()
        
        player.move(player.direction)
        player.update()
        shield.mouse()
        
        level.update()
        level.draw()
        shield.draw()
        player.draw()
        
        pygame.display.flip()

main()
