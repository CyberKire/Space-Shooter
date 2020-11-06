import sys  #Used to exit the game when the player quits
import pygame

def check_events():
    #  Queue for keyboard/mouse actions
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Check if we press the close button on the top corner of the display window
            sys.exit()

#  Update images on the screen and flip to the new screen.
def update_screen(game_settings, screen,ship):
    # Redrawing the screen on each loop
    screen.fill(game_settings.background_color)
    ship.blitme()

    #  Making the screen visible
    pygame.display.flip()