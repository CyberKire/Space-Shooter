import pygame  #Contains the functionality needed to make a game
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()  #Initializes the background settings that Pygame needs to work properly
    game_settings=Settings()
    screen=pygame.display.set_mode((game_settings.screen_width,game_settings.screen_height))  #Create display window to draw all of the game's elements
    pygame.display.set_caption("Space Shooter")

    # Making the ship of the game
    ship=Ship(game_settings,screen)

    #Make a group to store bullets in
    bullets=Group()

    #Main loop of the game
    while True:
        gf.check_events(game_settings,screen,ship,bullets)  #Used to check buttons/mouse pressed
        ship.update()  #Updates the position of the ship depending on the button pressed
        gf.update_bullets(bullets) #Deleting the bullets that go off screen
        gf.update_screen(game_settings,screen,ship,bullets) #Update images on the screen and flip to the new screen

run_game()
