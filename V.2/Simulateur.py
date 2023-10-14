    ################################################ 
    #marche sous version python 3.2 et pygame 1.9.2#
    ################################################
    #Version de test
    
#!/usr/bin/python

from turtle import position
import pygame, sys, os, time, datetime, csv #importation des fonction nécessaire.
import random as rd
import pandas as pd
from math import *
from pygame.locals import * #compilation Module pygame.

from M_screen import * #compilation Module screen.

from M_font import *

from M_clock import *


class Calcul():

	global nb_step, nb_planet, accuracy, file_path, file_name

	def __init__(self):

		self.entity = {}

		for planet in range(nb_planet):

			position_x = rd.randint(0,900)
			position_y = rd.randint(0,700)
			velocity_x = rd.random()*0.2-0.1
			velocity_y = rd.random()*0.2-0.1
			mass = rd.randint(10e7,10e10)
			volumic_mass = 5.515e6

			self.entity[str(planet)] = [position_x, position_y, velocity_x, velocity_y, mass, volumic_mass]

		self.t = []

		self.G = 6.674e-11

		self.save()

		print(sum(self.t)/len(self.t))

	def calcul(self):

		for planet in range(nb_planet):
			t1 = time.time()

			position_x = self.entity[str(planet)][0] 
			position_y = self.entity[str(planet)][1] 
			velocity_x = self.entity[str(planet)][2] 
			velocity_y = self.entity[str(planet)][3]
			mass = self.entity[str(planet)][4]
			volumic_mass = self.entity[str(planet)][5]

			# Calcule Préliminaire

			volum_planet = mass / volumic_mass # Calcule du volume de la planet
			radius_planet = pow((volum_planet/(4/3*pi)),1/3) # calcule du rayon de la planet

			for other_planet in range(nb_planet):
				if other_planet != planet:

					# Calucle Secondaire

					dist_planet_other_planet = sqrt((self.entity[str(other_planet)][0]-position_x)**2  +  (self.entity[str(other_planet)][1]-position_y)**2) # distance entre 2 planetes
					volum_other_planet = self.entity[str(other_planet)][4] / self.entity[str(other_planet)][5] # Calcule du volume de la planet

					a = self.G  * ( (self.entity[str(other_planet)][4]*mass)  /  dist_planet_other_planet)  /  mass # calcule Force de gravitation
					velocity_x += (self.entity[str(other_planet)][0]-position_x)/sqrt(((self.entity[str(other_planet)][0]-position_x)**2)+sqrt((self.entity[str(other_planet)][1]-position_y)**2))*a*accuracy # calcule acceleration en x
					velocity_y += (self.entity[str(other_planet)][1]-position_y)/sqrt(((self.entity[str(other_planet)][1]-position_y)**2)+sqrt((self.entity[str(other_planet)][0]-position_x)**2))*a*accuracy # calcule acceleration en y

					radius_other_planet = pow((volum_other_planet/(4/3*pi)),1/3) # Calcule du rayon de l'autre planet

					# Calcule Collision

					if radius_planet + radius_other_planet >= dist_planet_other_planet: # Calcule Détection

						# Calcule Réaction

						tang = (position_x - self.entity[str(other_planet)][0]) / position_y - self.entity[str(other_planet)][1] 

						velocity_x = -velocity_x
						velocity_y = -velocity_y

			# Calcul Finale

			position_x += velocity_x
			position_y += velocity_y

			# Enregistrement

			self.entity[str(planet)][0] = position_x
			self.entity[str(planet)][1] = position_y
			self.entity[str(planet)][2] = velocity_x
			self.entity[str(planet)][3] = velocity_y

			t2 = time.time()
			self.t.append(t2-t1)

	def save(self):

		header = ['position_x', 'position_y', 'velocity_x', 'velocity_y', 'mass', "volumic_mass"]

		print("Début du Calcul")
		t1 = time.time()

		for self.step in range(nb_step):
			self.calcul()

			for num in range(len(header)):
				file_name = str(header[num])+".csv"

				with open(os.path.join(file_path,file_name), 'a', encoding='UTF8') as f:
					writer = csv.writer(f, delimiter=',')

					# write the header

					data =  (self.entity[str(planet)][num] for planet in range(nb_planet))
					writer.writerow(data)

		with open(os.path.join(file_path,"config.csv"), 'a', encoding='UTF8') as f:
			writer = csv.writer(f, delimiter=',')
			writer.writerow(["nb_step", "accuracy", "nb_planet", "sec_equal"])
			writer.writerow([nb_step,accuracy,nb_planet,sec_equal])

		t2 = time.time()
				
		print("Fin du Calcul en : "+str(t2-t1))

		input("Taper pour continuer : ")


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

				volum_planet = mass / volumic_mass # Calcule du volume de la planet
				circle_size = pow((volum_planet/(4/3*pi)),1/3)

				pygame.draw.circle(self.screen, (255,255,255), (position_x,position_y), circle_size)
				pygame.draw.line(self.screen, (255,0,0),(position_x,position_y), (position_x+velocity_x*100,position_y+velocity_y*100))

			pygame.display.update()
			print(step)
			time_finish = time.time()
			time.sleep(frame_clock(time_start, time_finish, fps)[0])
		t2 = time.time()
		print(t2-t1)

nb_step = 10000
accuracy = 1
nb_planet = 10
sec_equal = 100
fps = 50

diff = nb_step*nb_planet
temps_estim = diff*3.4171080589294434e-06*2 + nb_step*0.0005879149436950683 + nb_planet**2*0.0005879149436950683
temps_marche = nb_step/((1/accuracy)*sec_equal)

print("Difficulté de Calcule éstimé : "+str(diff))
print("Temps estimé : "+str(temps_estim))
print("Temps de fonctionnement :"+ str(temps_marche)+" seconde")

file_path = "/Users/maxime/OneDrive/programation/Python/Physique/Preject_1/V.2/DATA/"
if not os.path.exists(file_path+str(len(os.listdir(file_path)))):
	file_path = file_path+str(len(os.listdir(file_path)))
	os.makedirs(file_path)

Calcul()
Draw()