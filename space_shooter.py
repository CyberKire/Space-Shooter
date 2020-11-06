import pygame  #Contains the functionality needed to make a game

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()  #Initializes the background settings that Pygame needs to work properly
    game_settings=Settings()
    screen=pygame.display.set_mode((game_settings.screen_width,game_settings.screen_height))  #Create display window to draw all of the game's elements
    pygame.display.set_caption("Space Shooter")

    # Making the ship of the game
    ship=Ship(screen)

    #Main loop of the game
    while True:
        gf.check_events()  #Used to check buttons/mouse pressed
        gf.update_screen(game_settings,screen,ship) #Update images on the screen and flip to the new screen

run_game()
