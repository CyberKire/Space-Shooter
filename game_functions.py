import sys  #Used to exit the game when the player quits
import pygame
from bullet import Bullet

def check_keydown_events(event,game_settings,screen,ship,bullets):
    #Responding to keys when they are pressed down
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key==pygame.K_SPACE:
        #Creating a bullet and adding to the bullet group
        new_bullet=Bullet(game_settings,screen,ship)
        bullets.add(new_bullet)

def check_keyup_events(event,ship):
    #Responding to keys when they are up
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(game_settings,screen,ship,bullets):
    #  Queue for keyboard/mouse actions
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Check if we press the close button on the top corner of the display window
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,game_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

#  Update images on the screen and flip to the new screen.
def update_screen(game_settings, screen,ship,bullets):
    # Redrawing the screen on each loop
    screen.fill(game_settings.background_color)
    #Redrawing bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()

    #  Making the screen visible
    pygame.display.flip()