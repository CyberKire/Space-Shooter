import pygame

class Ship:
    def __init__(self,screen):
        self.screen=screen

        #  Loading the ship image and getting its rect(rectangular shape)
        self.image=pygame.image.load('images/bat.png')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        #  Setting the ship to start at the bottom center of the screen
        self.rect.centerx=self.screen_rect.centerx#  The x-coordinate of the ship's center equal to the screen rect's centerx
        self.rect.bottom=self.screen_rect.bottom# The y-cordinate of the ship's bottom equal to screen rect's bottom attribute

        # Movement Flags
        self.moving_right=False
        self.moving_left=False

    def update(self):
        #  Moving the ship to the right
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx-=1

    #  Draw the image to the screen at the position specified by self.rect
    def blitme(self):
        self.screen.blit(self.image,self.rect)