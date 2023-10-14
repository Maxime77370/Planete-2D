import pygame #importation des fonction nécessaire
from pygame.locals import *

def init_screen():
	fenetre_x = 900
	fenetre_y = 700
	screen = pygame.display.set_mode((fenetre_x,fenetre_y)) #création d'une screen
	pygame.display.set_caption("chargement") #nommé la screen

	return screen, fenetre_x, fenetre_y

def update_screen(screen, position):

	pygame.display.update()