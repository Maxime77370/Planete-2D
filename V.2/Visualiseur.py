    ################################################ 
    #marche sous version python 3.2 et pygame 1.9.2#
    ################################################
    #Version de test
    
#!/usr/bin/python

import pygame, sys, os, time, datetime, csv #importation des fonction nécessaire.
import random as rd
import pandas as pd
from math import *
from pygame.locals import * #compilation Module pygame.

from M_screen import * #compilation Module screen.

from M_font import *

from M_clock import *

class Draw:

	global nb_step, nb_planet, accuracy, file_path, file_name

	def __init__(self):

		pygame.init() #initialisation de pygame.
		print("pygame.init : OK")

		self.screen, self.fenetre_x, self.fenetre_y = init_screen() #initialisation Module screen.
		print("init_screen : OK")

		self.entity = {}

		self.get_save()
		self.annimation()

	def get_save(self):

		header = ['position_x', 'position_y', 'velocity_x', 'velocity_y', 'mass', 'volumic_mass']

		for planet in range(nb_planet):
			self.entity[str(planet)] = [0]*len(header)
			for x in range(len(header)):
				self.entity[str(planet)][x] = [0]*nb_step

		for num in range(len(header)):
			file_name = str(header[num])+".csv"

			with open(os.path.join(file_path,file_name), newline='') as f:

				reader = csv.reader(f)
				for x,raw in enumerate(reader):
					for planet in range(nb_planet):
						self.entity[str(planet)][num][x] = (raw[planet])


	def annimation(self):
		t1 = time.time()
		for step in range(0,nb_step, int(ceil(nb_step/(nb_step/((1/accuracy)*sec_equal))/fps))):
			time_start = time.time()
			self.screen.fill((0,0,0))
			for planet in range(nb_planet):

				position_x = float(self.entity[str(planet)][0][step])
				position_y = float(self.entity[str(planet)][1][step])
				velocity_x = float(self.entity[str(planet)][2][step])
				velocity_y = float(self.entity[str(planet)][3][step])
				mass = float(self.entity[str(planet)][4][step])
				volumic_mass = float(self.entity[str(planet)][5][step])

				circle_size = pow((mass/volumic_mass*3)/(4*pi),1/3)

				pygame.draw.circle(self.screen, (255,255,255), (position_x,position_y), circle_size)
				pygame.draw.line(self.screen, (255,0,0),(position_x,position_y), (position_x+velocity_x*100,position_y+velocity_y*100))

			pygame.display.update()
			print(step)
			time_finish = time.time()
			time.sleep(frame_clock(time_start, time_finish, fps)[0])
		t2 = time.time()
		print(t2-t1)
	
fps = 50
masse_min = 10e6

file_path = "DATA/" + str(input("Quel simulation souhaitez-vous charger : "))

with open(os.path.join(file_path,"config.csv"), newline='') as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        nb_step = int(row["nb_step"])
        accuracy = float(row["accuracy"])
        nb_planet = int(row["nb_planet"])
        sec_equal = float(row["sec_equal"])

if input("Voulez-vous changer la vitesse (y/n) :") == 'y':
    sec_equal = float(input("La vitesse est configurer sur "+str(sec_equal)+", quel est la nouvelle valeur :"))

temps_marche = nb_step/((1/accuracy)*sec_equal)
print("Temps de fonctionnement :"+ str(temps_marche)+" seconde")

Draw()