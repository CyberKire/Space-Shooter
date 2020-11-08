import pygame

class Ship:
    def __init__(self,game_settings,screen): #screen is game screen
        self.screen=screen
        self.game_settings=game_settings
        #  Loading the ship image and getting its rect(rectangular shape)
        self.image=pygame.image.load('images/bat.png')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        #  Setting the ship to start at the bottom center of the screen
        self.rect.centerx=self.screen_rect.centerx#  The x-coordinate of the ship's center equal to the screen rect's centerx
        self.rect.bottom=self.screen_rect.bottom# The y-cordinate of the ship's bottom equal to screen rect's bottom attribute

        # Store a decimal value for the ship's center
        self.center=float(self.rect.centerx)

        # Movement Flags
        self.moving_right=False
        self.moving_left=False

    def update(self):
        #  Moving the ship to the right and left
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.center += self.game_settings.ship_speed_factor
        if self.moving_left and self.rect.left>0:
            self.center -= self.game_settings.ship_speed_factor

        #Updating rect(ship) object from self.center
        self.rect.centerx = self.center

    #  Draw the image to the screen at the position specified by self.rect
    def blitme(self):
        self.screen.blit(self.image,self.rect)