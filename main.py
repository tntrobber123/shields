import pygame
import random
import math

from window import Window
window = Window()

from player import Player
player = Player()

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
                    player.move = "up"
                    player.amount += 2
                if event.key == pygame.K_s:
                    player.move = "down"
                    player.amount += 2
                if event.key == pygame.K_a:
                    player.move = "left"
                    player.amount += 2
                if event.key == pygame.K_d:
                    player.move = "right"
                    player.amount += 2
                    
                if event.key == pygame.K_SPACE:
                    pass
                	
            if event.type == pygame.KEYUP:
                player.move = "null"
                player.amount -= 2
                player.moving = False
                    
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
        
        player.movement()
        	
        window.fill(WHITE, window.screen)
        player.draw()
        pygame.display.flip()

main()
