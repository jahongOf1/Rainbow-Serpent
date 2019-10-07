import pygame as pg
import time, sys
import random
import cx_Freeze

vec = pg.math.Vector2

pg.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)

img_red = "redball.png"
img_blue = "blueball.png"
img_green = "greenball.png"


gameDisplay = pg.display.set_mode((display_width, display_height))
pg.display.set_caption('Rainbow Serpent')
clock = pg.time.Clock()

x = display_width // 2
y = display_height // 2

x_change = 0
y_change = 0

orb_width = 65
orb_height = 65

end = False
	
color = img_blue
def player(color, x, y):
	orb = pg.image.load(color)
	gameDisplay.blit(orb, (x, y))


def quitgame():
    pg.quit()
    sys.exit()

while not end:
	for event in pg.event.get():
		# print(event)

		if event.type == pg.QUIT:
			quitgame()
		if event.type == pg.KEYDOWN:
			if event.key == pg.K_LEFT:
				x_change = -5
			if event.key == pg.K_RIGHT:
				x_change = 5
			if event.key == pg.K_UP:
				y_change = -5
			if event.key == pg.K_DOWN:
				y_change = 5
			if event.key == pg.K_z:
				color = img_red
			if event.key == pg.K_x:
				color = img_blue
			if event.key == pg.K_c:
				color = img_green

		if event.type == pg.KEYUP:
			if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
				x_change = 0
			if event.key == pg.K_UP or event.key == pg.K_DOWN:
				y_change = 0
		# if 
	x += x_change
	y += y_change
	y_change += 0.05
	# gameDisplay.fill()
	# gameDisplay.fill(white)
	player(color, x, y)
	pg.display.update()
	clock.tick(60)

quitgame()