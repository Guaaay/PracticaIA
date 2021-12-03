import pygame, sys, random
from pygame.locals import *
from car import Car
pygame.init()
 
# Colours

RS = 15 #RADIUS_STATION 
RS2 = RS/2

STATION_1 = [112,348]
STATION_2 = [358,349]
STATION_3 = [491,232]
STATION_4 = [615,103]
STATION_5 = [615,400]
STATIONS = [STATION_1, STATION_2, STATION_3, STATION_4, STATION_5]

car_0 = Car(id = 0, pos = [STATION_1[0], STATION_1[1]])


# Game Setup
FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 800
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
        pygame.quit()
        sys.exit()

      if event.type == pygame.MOUSEBUTTONUP:
        pos = pygame.mouse.get_pos()
        print(pos)
    # Processing
    # This section will be built out later

    # Render elements of the game
    WINDOW.fill(BACKGROUND)

    #pygame.draw.circle(surface, colour, center, radius, width)
    #pygame.draw.line(surface, colour, (startX, startY), (endX, endY), width)
    previous_station = STATIONS[0]
    for e in STATIONS:
      pygame.draw.circle(WINDOW, RED, e, RS )
      pygame.draw.line(WINDOW, RED, previous_station, e, 5)
      #pygame.draw.circle(WINDOW, WHITE, e, RS-3)
      previous_station = e

    
    

    #Vagón metro

    pygame.draw.circle(WINDOW, BLUE, car_0.pos, RS2 )

    car_0.move_to(dest=STATION_2)



    pygame.display.update()
    fpsClock.tick(FPS)
 
main()

    
