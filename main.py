#! /usr/bin/env python
import pygame
from pygame.locals import *
from sys import exit
from random import randrange
from src.population import *
import sys

WHITE		= (255, 255, 255)
BLACK		= (  0,   0,   0)
BLUE		= (  0,   0, 255)
GREEN		= (  0, 255,   0)
RED			= (255,   0,   0)
ORANGE		= (255, 165,   0)
GREY		= (128, 128, 128) 
YELLOW		= (255, 255,   0)
PINK		= (255, 192, 203)
LBLUE 		= (191, 238, 244)
BOARD_L		= (219, 202, 142)
BOARD_D		= ( 58,  41,  14)	

pygame.init()

if(len(sys.argv) < 5):
	n = 50
	k = 40
	e = 6
	m = 0.5
else:
	n = int(sys.argv[1])
	k = int(sys.argv[2])
	e = int(sys.argv[3])
	m = float(sys.argv[4])

assert(n == 10 or n == 20 or n == 30 or n == 50)
assert(k%2 == 0)
assert(e%2 == 0)
assert(m < 1.0 and m > 0.0)

screen_size = 900

screen = pygame.display.set_mode((screen_size, screen_size), 0, 32)
screen.fill(WHITE)

pygame.display.set_caption('Genetic Queens')

pop = Population(k, n, e, m)
target = (n*(n-1))/2

clock = pygame.time.Clock()

snap = math.floor(screen_size/n)

achou = False
generation = 0
pygame.font.init()
myfont = pygame.font.SysFont('Sans Serif', math.ceil(snap*1.5))

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()
		
	#construir board	

	for i in range(n):
		for j in range(n):
			if (i+j)%2 == 0:
				pygame.draw.rect(screen, BOARD_D, [i*snap, j*snap, snap, snap])
			else:
				pygame.draw.rect(screen, BOARD_L, [i*snap, j*snap, snap, snap])

	if not achou:
		pop.iteration()
		generation += 1
		res = pop.get_best()
		if res.fitness() == target:
			achou = True
			print("Acabou! =)")
		
	for i in range(len(res.values)):
		j = res.values[i]
		pygame.draw.circle(screen, BLUE, [i*snap + math.ceil(snap/2), j*snap + math.ceil(snap/2)], math.ceil(snap/3))
	
	if achou:
		textcolor = GREEN
	else:
		textcolor = RED
	textsurface = myfont.render('Generation: ' + str(generation), False, textcolor)
	screen.blit(textsurface, (0,0))


	pygame.display.update()
	time_passed = clock.tick(30)
