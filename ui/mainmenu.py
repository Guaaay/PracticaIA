#!/usr/bin/python3.4
# Setup Python ----------------------------------------------- #
from os import sendfile
import pygame, sys

from cte import *
from pygame.locals import *

from math import atan2, cos, degrees, radians, sin
import pygame.gfxdraw

lines = []
clicked = []
stations = pygame.sprite.Group()     


class Boton(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.test = 0
        self.image = start_normal
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
    def pressed(self):        
        self.image = start_press

    def hover(self):
        self.image = start_hover

    def no_hover(self):
        self.image = start_normal
   
        
class Station(pygame.sprite.Sprite):
    def __init__(self, id, coord):
        pygame.sprite.Sprite.__init__(self)
        
        self.test = 0
        self.id = id
        self.img = pygame.image.load(os.path.join(img_folder,f"estaciones/{id}.png"))
        self.image = pygame.transform.scale(self.img, (60,60)) 
        self.rect = self.image.get_rect()
        self.rect.center = coord
        self.selected = False
    
    def select(self):
        if self.selected:
            self.img = pygame.image.load(os.path.join(img_folder,f"estaciones/{self.id}.png"))
            self.image = pygame.transform.scale(self.img, (60,60))             
        else:           
            self.img = pygame.image.load(os.path.join(img_folder,f"estaciones/{self.id}s.png"))
            self.image = pygame.transform.scale(self.img, (60,60)) 
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
        self.color = YELLOW
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




#Devuelve la linea con los extremos en esas estaciones
def get_line(origin, dest):
    for l in lines:            
        if (l.origin == origin and l.dest == dest) or (l.origin == dest and l.dest == origin):                     
            return l

#Devuelve la ruta para ir de una estación a otra
def calculate_route(origin, dest):
    #Aquí se llamaría a la función que nos devuelve el map con las líneas a cambiar de color
    return {'114':113, '113':112, '112':111, '111':110}


#Selecciona las lineas de una ruta y les cambia el color
def select_lines(route):    
    for e in route:
        l = get_line(str(e),str(route[e]))        
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
    all_sprites = pygame.sprite.Group()    
    button = Boton()
    all_sprites.add(button)


    while True:        
        screen.fill(WHITE)
        draw_text('main menu', font, (255, 255, 255), screen, 20, 20)
 
        mx, my = pygame.mouse.get_pos()
 
        all_sprites.draw(screen)

        if button.rect.collidepoint((mx, my)):
            button.hover()            
            if click:
                
                button.pressed()           
                screen.fill(WHITE)                
                all_sprites.draw(screen)
                pygame.display.update()
                
                pygame.time.delay(300)
                game()
    
        else:
            button.no_hover()
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
        button.hover
        all_sprites.draw(screen)
        pygame.display.update()
        mainClock.tick(60)


 
def game():
    
    
   
    for e in estaciones:        
        pos_e = estaciones[e]
        stations.add(Station(e, pos_e))    

    for i in range (110,127):
        lines.append(line(str(i),str(i+1), RED))
    for i in range (210,227):
        lines.append(line(str(i),str(i+1), BLUE))
    for i in range (310,327):
        lines.append(line(str(i),str(i+1), GREEN))
   
    for l in lines:           
            DrawThickLine(screen, estaciones[l.origin], estaciones[l.dest], 6, l.color) 
            pygame.display.update()            

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

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                print(pos)
                for s in stations:
                    if s.rect.collidepoint(pos):
                        select_station(s)
                        
                        
                    
            
                    
                
                

        screen.fill(WHITE)

        #lineas
       
        for l in lines:          
            DrawThickLine(screen, estaciones[l.origin], estaciones[l.dest], 6, l.color) 
            #pygame.draw.line(screen, l.color, estaciones[l.origin], estaciones[l.dest], 10)   
            
        
       
        
        draw_text('game', font, (255, 255, 255), screen, 20, 20)
       
        #River
        DrawThickLine(screen, (1251, 0) ,(1251,726), 20, WATER)    
        DrawThickLine(screen, (1255,715) ,(1190,800), 20, WATER)    
        DrawThickLine(screen, (1195,785) ,(1195,1080), 20, WATER)   


        stations.draw(screen)        
        pygame.display.flip()
        pygame.display.update()
        mainClock.tick(60)
 
 
#main_menu()
game()

