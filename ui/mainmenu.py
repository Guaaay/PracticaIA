#!/usr/bin/python3.4
# Setup Python ----------------------------------------------- #

import pygame, sys
from pygame import mixer
from cte import *
from pygame.locals import *
from math import atan2, cos, degrees, radians, sin
import pygame.gfxdraw
from algoritmo import * 
#from algoritmo import *
from pathlib import Path

clock = pygame.time.Clock()
lines = []
clicked = []
stations = pygame.sprite.Group()     
FPS = 60
SIZE = WIDTH, HEIGHT = 1920, 1080

mixer.init()
mixer.music.load(Path("../resources/music/anthem.mp3"))
mixer.music.set_volume(0.1)
mixer.music.play()

class BotonStart(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = start_normal
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2.446, HEIGHT/1.8)
    def pressed(self):        
        self.image = start_press

    def hover(self):
        self.image = start_hover

    def no_hover(self):
        self.image = start_normal

class BotonCredits(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = creditos_normal
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 1.693, HEIGHT/1.8)
    def pressed(self):        
        self.image = creditos_press

    def hover(self):
        self.image = creditos_hover

    def no_hover(self):
        self.image = creditos_normal
    
class Titulo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.img = titulo
        self.image = self.image = pygame.transform.scale(self.img, (2000,2000)) 
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT/4)
    
class MenuBackground(pygame.sprite.Sprite):
    def __init__(self, position, images):
        super(MenuBackground, self).__init__()
        size = (WIDTH, HEIGHT)
        self.rect = pygame.Rect(position, size)
        self.images = images
        self.images_right = images
        self.index = 0
        self.image = images[self.index]  # 'image' is the current image of the animation.

        self.animation_time = 0.1
        self.current_time = 0

        self.animation_frames = 6
        self.current_frame = 0


class GameBackground(pygame.sprite.Sprite):
    def __init__(self, position, image):
        super(GameBackground, self).__init__()
        size = (WIDTH, HEIGHT)
        self.rect = pygame.Rect(position, size)
        self.image = image

    def update(self,dt):
        """This is the method that's being called when 'botonstart.update(dt)' is called.""" 
        # Switch between the two update methods by commenting/uncommenting.
        self.update_time_dependent(dt)
        # self.update_frame_dependent()

    def update_time_dependent(self, dt):
        """
        Updates the image of Sprite approximately every 0.1 second.

        Args:
            dt: Time elapsed between each frame.
        """

        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]

class Tren(pygame.sprite.Sprite):
    def __init__(self, position, images):
        super(Tren, self).__init__()
        size = (100, 100)
        self.rect = images[0].get_rect()
        self.rect.center = (position)
        self.images = images
        self.images_right = images
        self.index = 0
        self.image = images[self.index]  # 'image' is the current image of the animation.

        self.animation_time = 0.1
        self.current_time = 0

        self.animation_frames = 6
        self.current_frame = 0
    def update(self,dt):
        """This is the method that's being called when 'botonstart.update(dt)' is called.""" 
        # Switch between the two update methods by commenting/uncommenting.
        self.update_time_dependent(dt)
        # self.update_frame_dependent()

    def update_time_dependent(self, dt):
        """
        Updates the image of Sprite approximately every 0.1 second.

        Args:
            dt: Time elapsed between each frame.
        """

        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]



class Station(pygame.sprite.Sprite):
    def __init__(self, id, coord):
        pygame.sprite.Sprite.__init__(self)
        
        self.test = 0
        self.id = id
        self.img = pygame.image.load(Path(f"../resources/art/estaciones/{id}.png"))
        self.image = pygame.transform.scale(self.img, (90,90)) 
        self.rect = self.image.get_rect()
        self.rect.center = (coord[0], coord[1])
        self.selected = False
    
    def select(self):
        if self.selected:
            self.img = pygame.image.load(Path(f"../resources/art/estaciones/{self.id}.png"))
            self.image = pygame.transform.scale(self.img, (90,90))             
        else:           
            self.img = pygame.image.load(Path(f"../resources/art/estaciones/{self.id}s.png"))
            self.image = pygame.transform.scale(self.img, (90,90)) 
        self.selected = not self.selected

        
class line():
    def __init__(self, origin, dest, color):       
        #origin y est es un int con el número de estación     
        self.origin = origin
        self.dest = dest  
        self.defaultColor = color   
        self.color = color
        self.marked = False

    def select(self):
        self.color = (102,57,49)
    def deselect(self):
        self.color = self.defaultColor

#-----------------------------------------------------------------
#Aux functions for drawing lines using rotated rectangles
def Move(rotation, steps, position):
    """Return coordinate position of an amount of steps in a direction."""
    xPosition = cos(radians(rotation)) * steps + position[0]
    yPosition = sin(radians(rotation)) * steps + position[1]
    return (xPosition, yPosition)

def DrawThickLine(surface, point1, point2, thickness, color):
    angle = degrees(atan2(point1[1] - point2[1], point1[0] - point2[0]))

    vertices = list()
    vertices.append(Move(angle-90, thickness, point1))
    vertices.append(Move(angle+90, thickness, point1))
    vertices.append(Move(angle+90, thickness, point2))
    vertices.append(Move(angle-90, thickness, point2))

    pygame.gfxdraw.aapolygon(surface, vertices, color)
    pygame.gfxdraw.filled_polygon(surface, vertices, color)
#-----------------------------------------------------------------

#carga las imagenes de un directorio y devuelve una lista
def load_images(path):
    images = []
    for file_name in os.listdir(path):
        image = pygame.image.load(str(path) + os.sep + file_name)
        images.append(image)
    return images




#Devuelve la linea con los extremos en esas estaciones
def get_line(origin, dest):
    for l in lines:            
        if (l.origin == origin and l.dest == dest) or (l.origin == dest and l.dest == origin):                     
            return l

#Devuelve la ruta para ir de una estación a otra
def calculate_route(origin, dest): 
    #Aquí se llamaría a la función que nos devuelve el map con las líneas a cambiar de color
    print(int(origin.id))
    print(int(dest.id))
    algoritmo = Algoritmo(int(origin.id),int(dest.id), adjacent_stations)
    ruta = algoritmo.best_route() # Ahora conseguimos una lista de estaciones por las q hemos pasado
    for i, est in enumerate(ruta):
        ruta[i] = lines_stations_number[ruta[i]] # traduciendo nombre de estacion a nº
    # result = {}
    # for e in ruta:
    #    result[lines_stations_number[e]] = lines_stations_number[ruta[e]]
    # result = {value : key for (key, value) in result.items()}
    # print(result)
    print(ruta)
    return ruta


#Selecciona las lineas de una ruta y les cambia el color

def select_lines(route): 
    print("---------------------", route)   

    for i in range(0, len(route)-1):
        l = get_line(str(route[i]),str(route[i+1]))     
           
    #for e in route:
        #l = get_line(str(e),str(route[e]))        

        if (l is not None): 
            l.select()
            pygame.time.delay(500)
            DrawThickLine(screen, estaciones[l.origin], estaciones[l.dest], 6, l.color)             
            pygame.display.update()


#Cambia el color de las estaciones al seleccionarlas
def select_station(s):
            if(len(clicked)==2):
                clicked[0].select()
                clicked[1].select() 
                clicked.clear()  
                deselect_all_lines()  

            s.select()
            stations.draw(screen) 
            pygame.display.update()

            if s in clicked:                
                clicked.remove(s)
            else:
                clicked.append(s)
            
            if(len(clicked)==2):
                select_lines(calculate_route(clicked[0], clicked[1])) 

def deselect_all_lines():
    for line in lines:
        line.deselect()
        
 
# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()

pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((WIDTH, HEIGHT),0,32)
 
font = pygame.font.SysFont(None, 20)
 
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
click = False
 
def main_menu():
    botonstart = pygame.sprite.Group()
    botoncreditos = pygame.sprite.Group()
    startButton = BotonStart()
    creditsButton = BotonCredits()
    titulo = Titulo()
    botonstart.add(startButton)
    botoncreditos.add(creditsButton)
    images_bg = load_images(path=Path('../resources/art/background_menu'))
    images_tren = load_images(path=Path('../resources/art/tren'))
    fondo = MenuBackground(position=(0, 0), images=images_bg)
    tren = Tren(position = (WIDTH/2,HEIGHT/1.2),images = images_tren)
    bg_sprites = pygame.sprite.Group()
    bg_sprites.add(fondo)
    bg_sprites.add(titulo)
    bg_sprites.add(tren)
    click = False
    

    while True:
        dt = clock.tick(FPS) / 1000
        draw_text('main menu', font, (255, 255, 255), screen, 20, 20)
 
        mx, my = pygame.mouse.get_pos()
 
        botonstart.draw(screen)

        if startButton.rect.collidepoint((mx, my)):
            startButton.hover()     
            if click:
                startButton.pressed()                           
                botonstart.draw(screen)
                pygame.display.update()
                
                pygame.time.delay(500)
                game()
    
        else:
            startButton.no_hover()
        if creditsButton.rect.collidepoint((mx, my)):
            creditsButton.hover()     
            if click:
                creditsButton.pressed()                           
                botoncreditos.draw(screen)
                pygame.display.update()
                
                pygame.time.delay(300)
                game()
    
        else:
            creditsButton.no_hover()

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        startButton.hover
        bg_sprites.update(dt)
        bg_sprites.draw(screen)
        botonstart.draw(screen)
        botoncreditos.draw(screen)
        pygame.display.update()
        mainClock.tick(60)
 
def game():
    
    game_back = GameBackground(position = (0,0),image = game_background)
    bg_game = pygame.sprite.Group()
    bg_game.add(game_back)
    
   
    for e in estaciones:        
        pos_e = estaciones[e]
        stations.add(Station(e, pos_e))    

    for i in range (110,127):

        lines.append(line(str(i),str(i+1), RED))

    for i in range (210,227):
        lines.append(line(str(i),str(i+1), BLUE))

    for i in range (310,327):
        if(i!=312 and i!= 319 and i!= 313 and i!=320):
            lines.append(line(str(i),str(i+1), GREEN))
    lines.append(line(str(312),str(314), GREEN))    
    lines.append(line(str(319),str(321), GREEN))



    for l in lines:           
            DrawThickLine(screen, estaciones[l.origin], estaciones[l.dest], 12, l.color) 
            pygame.display.update()            

    click = False
    running = True
    while running:

        

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print(pos)
                for s in stations:
                    if s.rect.collidepoint(pos):
                        select_station(s)
                        
                        
                    
            
        bg_game.draw(screen)
        
                
          #River
        DrawThickLine(screen, (1251, 0) ,(1251,726), 20, WATER)    
        DrawThickLine(screen, (1255,715) ,(1190,800), 20, WATER)    
        DrawThickLine(screen, (1195,785) ,(1195,1080), 20, WATER)          

        
        #lineas
       
        for l in lines:          
            DrawThickLine(screen, estaciones[l.origin], estaciones[l.dest], 12, l.color) 
            #pygame.draw.line(screen, l.color, estaciones[l.origin], estaciones[l.dest], 10)   
            
        
       
        
        draw_text('game', font, (255, 255, 255), screen, 20, 20)
       
      


        stations.draw(screen)        
        pygame.display.flip()
        pygame.display.update()
        mainClock.tick(60)
 
 
main_menu()
game()

