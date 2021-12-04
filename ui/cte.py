import pygame, sys, os
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, '../resources/art')
start_normal = pygame.image.load(os.path.join(img_folder, 'start_normal.png'))
start_hover = pygame.image.load(os.path.join(img_folder, 'start_hover.png'))
start_press = pygame.image.load(os.path.join(img_folder, 'start_press.png'))

WIDTH = 1920  # width of our game window
HEIGHT = 1080 # height of our game window
# Colors (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WATER = (212,241,249)


estaciones_LR = {"110":(60, 569), "111":(130, 569), "112":(201, 569), "113":(272, 569), "114":(342, 569), "115":(412, 569), "116":(490, 569), 
"117":(574, 569), "118":(645, 569), "119":(740, 484), "120":(889, 484), "121":(1015, 484), "122":(1114, 484), "123":(1184, 415), "124":(1227, 371),
 "125":(1268, 331), "126":(1325, 274), "127":(1394, 204)}

estaciones_LA = {"210":(889, 35), "211":(889, 91), "212":(889, 147), "213":(889, 204), "214":(889, 275), "215":(889, 330),
 "216":(889, 383), "217":(889, 484), "218":(889, 628), "219":(889, 681), "220":(889, 750), "221":(889, 849), "222":(889, 932), 
 "223":(832, 990), "224":(704, 990), "225":(608, 990), "226":(518, 990), "227":(419, 990)}


estaciones_LV = {"310":(437, 203), "311":(494, 260), "312":(551, 314), "313":(624, 382), "314":(735, 486), "315":(888, 628), "316":(1085, 631), "317":(1142, 685), "318":(1196, 733), "319":(1242, 775),
"320":(1293, 826), "321":(1337, 866), "322":(1389, 914), "323":(1447, 971), "324":(1531, 974), "325":(1612, 974), "326":(1671, 915), "327":(1672, 825)}
estaciones = {}
estaciones.update(estaciones_LR)
estaciones.update(estaciones_LA)
estaciones.update(estaciones_LV)


alg = [110,111]
