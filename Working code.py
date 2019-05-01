#hope this code will work
#i just try the code it works
#let me add the control
#import libraries
import pygame
import sys
#initialize game
pygame.init()

#screen resolution
width = 1000
height = 850
#car boundary
car_size= 55

raceDisplay = pygame.display.set_mode((width,height))
pygame.display.set_caption('Speedy Run')

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()
speedover = False
car1 = pygame.image.load('car.png')
#def the main car
def car(x,y):
    raceDisplay.blit(car1, (x,y))
#measurement for car
x =  (width * 0.45)
y = (height * 0.8)

while not speedover:
   if event.type == pygame.KEYDOWN:
        	if event.key == pygame.K_LEFT:
        	  x-=100
        	elif event.key == pygame.K_RIGHT:
        		x+=100
        	elif event.key == pygame.K_UP:
        		y-=50
        	elif event.key == pygame.K_DOWN:
        		y+=50
        if x > width - car_size or x < 0:
        	speedover= True

        elif y>height - car_size or y< 0:
        	speedover = True
	 	e

        	car_position=[x,y]
#the control is working buy it goes like everywhere
# I am going to set up boundaries  and fix it so it stay in palce after we put the background
#backg fill
    raceDisplay.fill(white)
    car(x,y)

        if x > width - car_size or x < 0:
            speedover =True
        elif y>height - car_size or y< 0:
             speedover = True
    pygame.display.update()
    #frame per second
    clock.tick(60)
#end game 
pygame.quit()
quit()
