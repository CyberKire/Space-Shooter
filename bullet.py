import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,game_settings,screen,ship):
        #Creating the bullet object where the ship is positioned
        super().__init__()
        self.screen=screen

        #Creating a bullet rect at 0,0
        self.rect=pygame.Rect(0,0,game_settings.bullet_width,game_settings.bullet_height)
        self.rect.centerx=ship.rect.centerx
        self.rect.top=self.ship.top

        #Setting bullet position as a decimal
        self.y=float(self.rect.y)

        self.color=game_settings.bullet_color
        self.speed_factor=game_settings.bullet_speed_factor