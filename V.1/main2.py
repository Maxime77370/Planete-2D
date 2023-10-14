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

		self.planet_save = {}

		self.x_screen, self.y_screen = self.screen.get_size()

		self.masse_min = 10e11
		self.masse_max = 10e13

		self.px_to_m = 0.001

		self.nb_planet = 10

		for x in range(self.nb_planet):
			self.planet_save[str(x)] = [rd.randint(0,self.x_screen),rd.randint(0,self.y_screen)],[rd.randint(-10,10),rd.randint(-10,10)],rd.uniform(0.9,0.9), time.time(), rd.uniform(self.masse_min,self.masse_max)

		self.G = 6.67408e-11

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
				self.gravity(i[0], i[1][0], i[1][1], i[1][4])
			for i in self.planet_save.items():
				self.move(i[0], i[1][0], i[1][1], i[1][2], i[1][3], i[1][4])

			pygame.display.update()

			time_finish = time.time()

			print(frame_clock(time_start, time_finish))

	def gravity(self, x, position, velocity, masse):

		for i in self.planet_save.items():
			if i[1][0][0] != position[0] and i[1][0][1] != position[1]:
				if i[1][0][1]-position[1] >= 0 and i[1][0][0]-position[0] >= 0:
					angle = math.atan((i[1][0][1]-position[1])/(i[1][0][0]-position[0]))*180/math.pi
				elif i[1][0][1]-position[1] >= 0 and i[1][0][0]-position[0] <= 0:
					angle = -math.atan((i[1][0][1]-position[1])/(i[1][0][0]-position[0]))*180/math.pi
				elif i[1][0][1]-position[1] <= 0 and i[1][0][0]-position[0] >= 0:
					angle = -math.atan((i[1][0][1]-position[1])/(i[1][0][0]-position[0]))*180/math.pi
				elif i[1][0][1]-position[1] <= 0 and i[1][0][0]-position[0] <= 0:
					angle = math.atan((i[1][0][1]-position[1])/(i[1][0][0]-position[0]))*180/math.pi

				print(angle)

				velocity_x = self.G * masse * i[1][4] / ((i[1][0][0] - position[0])*self.px_to_m)*((angle-90)/90)
				velocity_y = self.G * masse * i[1][4] / ((i[1][0][1] - position[1])*self.px_to_m)*(angle/90)
				if velocity_x >= 0:
					velocity[0] += math.sqrt(velocity_x/masse)
				else:
					velocity[0] -= math.sqrt(-velocity_x/masse)
				if velocity_y >= 0:
					velocity[1] += math.sqrt(velocity_y/masse)
				else:
					velocity[1] -= math.sqrt(-velocity_y/masse)
		print(angle)

		self.planet_save[str(x)][1][0], self.planet_save[str(x)][1][1] = velocity[0], velocity[1]


	def move(self, x, position, velocity, rebond, time_1, masse):

		time_2 = time.time()
		position[0] += velocity[0] * (time_2-time_1)*self.px_to_m
		position[1] += velocity[1] * (time_2-time_1)*self.px_to_m
		time_1 = time.time()

		pygame.draw.circle(self.screen, (255,255,255), position, math.sqrt(masse/(self.masse_min)*math.pi))

		self.planet_save[str(x)] = position, velocity, rebond, time_1, masse

Play()