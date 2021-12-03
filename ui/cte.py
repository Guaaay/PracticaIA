import pygame, sys, os
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, '../resources/art')
start_normal = pygame.image.load(os.path.join(img_folder, 'start_normal.png'))
start_hover = pygame.image.load(os.path.join(img_folder, 'start_hover.png'))
start_press = pygame.image.load(os.path.join(img_folder, 'start_press.png'))

WIDTH = 1600  # width of our game window
HEIGHT = 1000 # height of our game window
# Colors (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


estaciones = {'110':(93, 456), '111':(158, 371), '112':(252, 311), '113':(380, 274), '114':(556, 270)}

alg = [110,111]
