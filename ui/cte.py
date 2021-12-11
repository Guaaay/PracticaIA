import pygame, sys, os
from pathlib import Path

#game_folder = os.path.dirname('.')
#img_folder = os.path.join(game_folder, '.\\resources\\art')
start_normal = pygame.image.load(Path('../resources/art/start_normal.png'))
start_hover = pygame.image.load(Path('../resources/art/start_hover.png'))
start_press = pygame.image.load(Path('../resources/art/start_press.png'))
creditos_normal = pygame.image.load(Path('../resources/art/creditos_normal.png'))
creditos_hover = pygame.image.load(Path('../resources/art/creditos_hover.png'))
creditos_press = pygame.image.load(Path('../resources/art/creditos_press.png'))
titulo = pygame.image.load(Path('../resources/art/titulo_practica.png'))
game_background = pygame.image.load(Path('../resources/art/gamebackgroundm.jpg'))
creditos = pygame.image.load(Path('../resources/art/marcocreditos.png'))
tiempo_imagen = pygame.image.load(Path('../resources/art/marcotiempo.png'))


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
"117":(574, 569), "118":(645, 569), "119":(740, 484), "120":(932, 485), "121":(1015, 484), "122":(1114, 484), "123":(1184, 415), "124":(1227, 371),
 "125":(1268, 331), "126":(1325, 274), "127":(1394, 204)}

estaciones_LA = {"210":(889, 35), "211":(889, 91), "212":(889, 147), "213":(889, 204), "214":(889, 275), "215":(889, 330),
 "216":(889, 383), "217":(889, 484), "218":(889, 585), "219":(889, 681), "220":(889, 750), "221":(889, 849), "222":(889, 932), 
 "223":(832, 990), "224":(704, 990), "225":(608, 990), "226":(518, 990), "227":(419, 990)}


estaciones_LV = {"310":(437, 203), "311":(494, 260), "312":(551, 314), "314":(707, 457), "315":(888, 628), "316":(1085, 631), "317":(1142, 685), "318":(1196, 733), "319":(1242, 775),
 "321":(1337, 866), "322":(1389, 914), "323":(1447, 971), "324":(1531, 974), "325":(1612, 974), "326":(1671, 915), "327":(1672, 825)}


estaciones = {}
estaciones.update(estaciones_LR)
estaciones.update(estaciones_LA)
estaciones.update(estaciones_LV)



map_estaciones = {110:[111], 111:[110,112], 112:[111,113], 113:[112, 114], 114:[113, 115], 115:[114, 116], 116:[115, 117], 117:[116, 118], 118:[117, 119], 119:[118, 120, 314], 120:[119, 121, 217], 121:[120, 122], 122:[121, 123], 123:[122, 124], 124:[123, 125], 126:[125, 127], 127:[126],
                210:[211], 211:[210,212],212:[211,213],213:[212,214],214:[213,215],215:[214,216],216:[215,217],217:[216,120,218],218:[217,315,219],219:[218,220],220:[219,221],221:[220,222],222:[221,223],223:[222,224],224:[223,225],225:[224,226],226:[225,227],227:[226],
                310:[311], 311:[310,312], 312:[311,314],314:[312,315,119],316:[315,317],317:[316,318],318:[317,319],
                327:[326],326:[325,327],325:[324,326],324:[323,325],323:[322,324],322:[321,323],321:[319,322],319:[318,321],318:[317,319],317:[316,318],316:[315,317],315:[218,316,314]}