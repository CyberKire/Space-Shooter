import sys  #Used to exit the game when the player quits
import pygame  #Contains the functionality needed to make a game

def run_game():
    pygame.init()  #Initializes the background settings that Pygame needs to work properly
    screen=pygame.display.set_mode((1200,800))  #Create display window to draw all of the game's elements
    pygame.display.set_caption("Space Shooter")
    background_color=(230,230,230)
    #Main loop of the game
    while True:
        #  Queue for keyboard/mouse actions
        for event in pygame.event.get():
            if event.type==pygame.QUIT:  #Check if we press the close button on the top corner of the display window
                sys.exit()

        screen.fill(background_color)
        #  Making the screen visible
        pygame.display.flip()

run_game()