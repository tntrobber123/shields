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
                    level.world_shifty = 5
                elif event.key == pygame.K_a:
                    player.direction = ("L")
                    level.world_shiftx = 5
                elif event.key == pygame.K_d:
                    player.direction = ("R")
                    level.world_shiftx = -5
                elif event.key == pygame.K_s:
                	player.direction = ("D")
                	level.world_shifty = -5
                	
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
        
        if shield.angle >= -20 and shield.angle <= 20:
            shield.speed = True
            if level.world_shiftx == 5:
                level.world_shiftx = 13
            if level.world_shiftx == -5:
                level.world_shiftx = -13
        else:
            shield.speed = False
            
            if level.world_shiftx == 13:
                level.world_shiftx = 5
            if level.world_shiftx == -13:
                level.world_shiftx = -5
        
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
