    ################################################ 
    #marche sous version python 3.2 et pygame 1.9.2#
    ################################################
    #Version de test
    
#!/usr/bin/python

import pygame, sys, os, math, time, datetime #importation des fonction nécessaire.
import random as rd
from pygame.locals import * #compilation Module pygame.

from M_screen import * #compilation Module screen.

from M_font import *

from M_clock import *

class Play():
	def __init__(self):

		pygame.init() #initialisation de pygame.
		print("pygame.init : OK")

		self.screen, self.fenetre_x, self.fenetre_y = init_screen() #initialisation Module screen.
		print("init_screen : OK")

		self.score_font = init_font()
		print("init_font : OK")

		self.planet_save = {}

		self.x_screen, self.y_screen = self.screen.get_size()

		for x in range(1):
			self.planet_save[str(x)] = [rd.randint(0,self.x_screen),rd.randint(0,self.y_screen)],[rd.randint(0,10),rd.randint(-50,50)],rd.uniform(0.9,0.9), time.time(), rd.uniform(10e4,10e5)

		self.gravity = 9.81

		self.boucle()

	def boucle(self):

		self.Play = True

		self.time = time.time()
		self.time_1 = time.time()

		while self.Play:

			time_start = time.time()

			self.screen.fill((0,0,0))

			for event in pygame.event.get(): #activation de la detection de touche.
				if event.type == QUIT : #si la vous appuyer sur le bouton de fermeture de fenetre.
					self.Play = False #arret de la boucle.
				elif event.type == KEYDOWN: #si boutton pression d'une touche.
					if event.key == K_ESCAPE: #si activation bouton echap.
						self.Play = False
					if event.key == K_a: #si activation bouton echap.
						self.__init__()

			for i in self.planet_save.items():
				self.move(i[0], i[1][0], i[1][1], i[1][2], i[1][3], i[1][4])

			pygame.display.update()

			time_finish = time.time()

			print(frame_clock(time_start, time_finish))

	def move(self, x, position, velocity, rebond, time_1, masse):

		time_2 = time.time()
		velocity[0] += -velocity[0] * 0 *(time_2 - time_1)
		velocity[1] += self.gravity * (time_2 - time_1)
		position[0] += velocity[0] * (time_2-time_1)*100
		position[1] += velocity[1] * (time_2-time_1)*100
		time_1 = time.time()


		if position[1] > self.y_screen:
			position[1] = self.y_screen
			velocity[1] = -velocity[1]*rebond

		if position[1] < 0:
			position[1] = 0
			velocity[1] = -velocity[1]*rebond

		if position[0] > self.x_screen:
			position[0] = self.x_screen
			velocity[0] = -velocity[0]*rebond

		if position[0] < 0:
			position[0] = 0
			velocity[0] = -velocity[0]*rebond

		pygame.draw.circle(self.screen, (255,255,255), position, masse/10e4)

		self.planet_save[str(x)] = position, velocity, rebond, time_1, masse

Play()