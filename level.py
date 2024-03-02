import pygame

from platforms import Platform
platform = Platform()

from window import Window
window = Window()

class Level(pygame.sprite.Sprite):
    def __init__(self):
        self.platform_list = pygame.sprite.Group()
        self.world_shift = 0
        self.world_shifty = 1
        self.level_limitx = -1000
        self.level_limity = 250
        
        self.background = pygame.image.load("sprites/background.png")
        
        self.level_limitx = -500
        self.level_limity = 500

        self.level_x = [ 
                  500, 500, 500
                  ]
                  
        self.level_y = [ 
                  500, 600, 700
                  ]

    # Update everything on this level
    def update(self):
        self.platform_list.update()

    def draw(self):

        window.screen.blit(self.background,(self.world_shift // 3, self.world_shifty))

        # Draw all the sprite lists that we have
        self.platform_list.draw(window.screen)

    def shift_world(self, shift_x):
        # Keep track of the shift amount
        self.world_shift += shift_x
        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x
            
            
    def shift_worldy(self, shift_y):
        self.world_shifty += shift_y
        for platform in self.platform_list:
            platform.rect.y += shift_y
            
    def shift_worldx(self, shift_x):
        self.world_shiftx += shift_x
        for platform in self.platform_list:
            platform.rect.x += shift_x

        # Go through the array above and add platforms
    def updateworld(self):
        for i in self.level:
            block.rect = self.level([i])
    
        for i in self.level:
            block.rect = self.level([i])
            block.player = self.player
            self.platform_list.add(self.block)

"""        
class Level_02(Level):

    def __init__(self, player):

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("background_02.png").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limitx = -1000
        self.level_limity = 250

        # Array with type of platform, and x, y location of the platform.
        level = [ [platforms.STONE_PLATFORM_LEFT, 500, 550],
                  [platforms.STONE_PLATFORM_MIDDLE, 570, 550],
                  [platforms.STONE_PLATFORM_RIGHT, 640, 550],
                  [platforms.GRASS_LEFT, 800, 400],
                  [platforms.GRASS_MIDDLE, 870, 400],
                  [platforms.GRASS_RIGHT, 940, 400],
                  [platforms.GRASS_LEFT, 1000, 500],
                  [platforms.GRASS_MIDDLE, 1070, 500],
                  [platforms.GRASS_RIGHT, 1140, 500],
                  [platforms.STONE_PLATFORM_LEFT, 1120, 280],
                  [platforms.STONE_PLATFORM_MIDDLE, 1190, 280],
                  [platforms.STONE_PLATFORM_RIGHT, 1260, 280],
                  ]


        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)
        
        # Create platforms for the level
class Level_03(Level):

    def __init__(self, player):

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("background_03.png").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limitx = -1000
        self.level_limity = 250
        
        # Array with type of platform, and x, y location of the platform.
        level = [ [platforms.STONE_PLATFORM_LEFT, 50, 50],
                  [platforms.STONE_PLATFORM_MIDDLE, 50, 50],
                  [platforms.STONE_PLATFORM_RIGHT, 640, 550],
                  [platforms.GRASS_LEFT, 50, 50],
                  [platforms.GRASS_MIDDLE, 870, 400],
                  [platforms.GRASS_RIGHT, 940, 400],
                  [platforms.GRASS_LEFT, 1000, 500],
                  [platforms.GRASS_MIDDLE, 1070, 500],
                  [platforms.GRASS_RIGHT, 1140, 500],
                  [platforms.STONE_PLATFORM_LEFT, 1120, 280],
                  [platforms.STONE_PLATFORM_MIDDLE, 1190, 280],
                  [platforms.STONE_PLATFORM_RIGHT, 1260, 280],
                  [platforms.GRASS_LEFT, 700, 870]
                  ]


        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)
            
class Level_04(Level):

    def __init__(self, player):

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("background_01.png").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limitx = -1500
        self.level_limity = 250

        # Array with type of platform, and x, y location of the platform.
        level = [
                  #Main platforms ingame
                  [platforms.GRASS_LEFT, 500, 530],
                  [platforms.GRASS_MIDDLE, 570, 530],
                  [platforms.GRASS_RIGHT, 640, 530],
                  [platforms.GRASS_LEFT, 800, 400],
                  [platforms.GRASS_MIDDLE, 870, 400],
                  [platforms.GRASS_MIDDLE, 940, 400],
                  [platforms.GRASS_RIGHT, 1010, 400],
                  [platforms.GRASS_LEFT, 1000, 530],
                  [platforms.GRASS_MIDDLE, 1070, 530],
                  [platforms.GRASS_RIGHT, 1140, 530]
                  ]


        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)
            """
