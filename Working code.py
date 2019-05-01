#hope this code will work
#import libraries
import pygame
import sys
#initialize game
pygame.init()

#screen resolution
width = 1000
height = 850

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
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            speedover = True
            sys.exit()
#backg fill
    raceDisplay.fill(white)
    car(x,y)

        
    pygame.display.update()
    #frame per second
    clock.tick(60)
#end game 
pygame.quit()
quit()
