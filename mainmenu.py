#!/usr/bin/python3.4
# Setup Python ----------------------------------------------- #
import pygame, sys
import os

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'resources\\art')
start_normal = pygame.image.load(os.path.join(img_folder, 'start_normal.png'))
start_hover = pygame.image.load(os.path.join(img_folder, 'start_hover.png'))
start_press = pygame.image.load(os.path.join(img_folder, 'start_press.png'))

WIDTH = 1000  # width of our game window
HEIGHT = 1000 # height of our game window
# Colors (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

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

 
# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *
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
            button.hover
            if click:
                button.pressed
                screen.fill(WHITE)
                all_sprites.draw(screen)
                pygame.display.update()
                pygame.time.delay(500)
                game()
 
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
    running = True
    while running:
        screen.fill((0,0,0))
        
        draw_text('game', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)
 
 
main_menu()