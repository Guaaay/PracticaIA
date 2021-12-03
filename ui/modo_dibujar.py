import pygame, sys, random
from pygame.locals import *
from car import Car
pygame.init()
 
# Colours
BACKGROUND = (255, 255, 255)
RED = (255, 30, 70)
BLUE = (10, 20, 200)
GREEN = (50, 230, 40)
WHITE = (255, 255, 255)

draw = []

bg = pygame.image.load("bg.png")



# Game Setup
FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
 
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('My Game!')
 
# The main function that controls the game
def main () :
  looping = True
  
  # The main game loop
  while looping :

    # Get inputs
    for event in pygame.event.get() :
      if event.type == QUIT :
        print(draw)
        pygame.quit()
        sys.exit()

      if event.type == pygame.MOUSEBUTTONUP:
        pos = pygame.mouse.get_pos()
        draw.append(pos)
        print(pos)
        
    # Processing
    # This section will be built out later

    # Render elements of the game
    WINDOW.fill(BACKGROUND)
    #WINDOW.blit(bg, (0, 0))
    for e in draw:
      pygame.draw.circle(WINDOW, RED, e, 15 )
      pygame.draw.circle(WINDOW, WHITE, e, 12 )
      pygame.draw.circle(WINDOW, BLUE, e, 3 )

    #pygame.draw.circle(surface, colour, center, radius, width)
    
    pygame.draw.line(WINDOW, RED, (0, pygame.mouse.get_pos()[1]),(WINDOW_WIDTH,pygame.mouse.get_pos()[1] ), 1)
    pygame.draw.line(WINDOW, RED, (pygame.mouse.get_pos()[0], 0),(pygame.mouse.get_pos()[0],WINDOW_HEIGHT), 1)
    pygame.display.update()
    fpsClock.tick(FPS)
 
main()


    
