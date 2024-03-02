import pygame
pygame.init()

class Window():
	screen_width = 1290
	screen_height = 700

	RED = (255, 0, 0)
	GREEN = (0, 255, 0)
	BLUE = (0, 0, 255)
	BLACK = (0, 0, 0)
    
	screen = pygame.display.set_mode((screen_width, screen_height))

	screen.fill(BLACK)
		
	def draw(self, screen):
		pygame.draw.circle(screen, color)
		
	def fill(self, color, screen):
		screen.fill(color)
		
	def update_display(self):
		pygame.display.flip();
