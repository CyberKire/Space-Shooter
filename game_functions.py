import sys  #Used to exit the game when the player quits
import pygame

def check_keydown_events(event,ship):
    #Responding to keys when they are pressed down
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

def check_keyup_events(event,ship):
    #Responding to keys when they are up
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ship):
    #  Queue for keyboard/mouse actions
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Check if we press the close button on the top corner of the display window
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

#  Update images on the screen and flip to the new screen.
def update_screen(game_settings, screen,ship):
    # Redrawing the screen on each loop
    screen.fill(game_settings.background_color)
    ship.blitme()

    #  Making the screen visible
    pygame.display.flip()