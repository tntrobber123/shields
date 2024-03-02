import pygame
import random
import math

from window import Window
window = Window()

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
                if event.key == pygame.K_LEFT:
                    pass
                if event.key == pygame.K_RIGHT:
                    pass
                if event.key == pygame.K_UP:
                    pass
                if event.key == pygame.K_DOWN:
                    pass
                    
                if event.key == pygame.K_SPACE:
                	pass
                    
                if event.key == pygame.K_ESCAPE:
                	pygame.quit()
                	quit()
        
        window.fill(WHITE, window.screen)
        
        pygame.display.flip()

main()
