import pygame
import sys
import random

pygame.init()

car_number_enemy= 150
car_size_enemy= 135
display_width = 1000
display_height = 800
car_position = [750,500]
car_position2 = [random.randint(0,display_width - car_size_enemy),0]
car_position3 = [random.randint(0,display_width - car_size_enemy),0]
speed_time=15

car_number_enemy= 150
car_size_enemy= 25

x = car_position[0]
y = car_position[1]

t = car_position2[0]
z = car_position2[1]

a = car_position3[0]
b = car_position3[1]




raceDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Speedy Run')

black = (0,0,0)
white = (255,255,255)

speed = False
clock = pygame.time.Clock()
car_Img = pygame.image.load('car2.png')
car_Img2 = pygame.image.load('car1.jpg')
car_Img3 = pygame.image.load('car3.png')

def pause():

        pause = True

        while paused:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()

                        if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_c:
                                        puased = False

                                elif event.key == pygame.K_q:
                                        pygame.quit()
                                        quit()
					
def car1(x,y):
    raceDisplay.blit(car_Img, (car_position[0],car_position[1]))

def car2(t,z):
    raceDisplay.blit(car_Img2, (car_position2[0],car_position2[1]))

def car3(a,b):
    raceDisplay.blit(car_Img3, (car_position3[0],car_position3[1]))

def car4(c,d):
    raceDisplay.blit(car_Img4, (car_position4[0],car_position4[1]))

def car_crash(car_position,car_position2,car_position3)

	if ((t, a >= x and t, a < x ) or ((x >= t, a and x < t, a)):
    	if (( z, b > y  and z,b < y) or (y >= z,b and y < z,b)):
    		return True
    reurn False 

while not speed:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
        	if event.key == pygame.K_LEFT:
        	  x-=100
        	elif event.key == pygame.K_RIGHT:
        		x+=100
        	elif event.key == pygame.K_UP:
        		y-=100
        	elif event.key == pygame.K_DOWN:
        		y+=100

        	car_position=[x,y]	


    raceDisplay.fill(white)

    if car_position2[1]>=0 and car_position2[1] < display_height:
    	car_position2[1] +=speed_time

    else:
    	car_position2[0]= random.randint(0,display_width - car_size_enemy)
    	car_position2[1] = 1

    if car_position3[1]>=0 and car_position3[1] < display_height:
    	car_position3[1] +=speed_time
    else:
    	car_position3[0]= random.randint(0,display_width - car_size_enemy)
    	car_position3[1] = 1
    if car_crash(car_position,car_position2,car_position3):
    	game_over= True
    	break


    car1(x,y)
    car2(t,z)
    car3(a,b)
    

    clock.tick(15)
        
    pygame.display.update()
    

pygame.quit()
quit()
