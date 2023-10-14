import pygame, sys #importation des fonction nécessaire
from pygame.locals import *

def init_font():

	font_1 = pygame.font.SysFont("dpcomic.ttf", 50)

	return font_1

def font_score(font_1, score_nb, fps):

	score = font_1.render('%d' % score_nb, True, (255, 255, 255))
	fps_font = font_1.render('%d' % fps, True, (255, 255, 255))

	return score, fps_font