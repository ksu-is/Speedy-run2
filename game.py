# import pygame from library
import pygame

pygame.init()
# size and set the main display of the game.
#adding variable for screen resolution'
width = 1000
height = 850 
raceDisplay = pygame.display.set_mode((width,height))
pygame.display.set_caption('Speedy Run')
#adding the color for our screen
black = (0,0,0)
white = (255,255,255)

# This is for frame per second of the game. If we put high value in the () The game goes more smoothly.
clock = pygame.time.Clock()

speed = False
#loading car image
car1 = pygame.image.load('car1.png')
#def the car1
def car1(x,y):
    gameDisplay.blit(car1, (x,y))
#make the starting point of our car
x= 500
y= 100

while not speed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            speed = True
#make the backg color
raceDisplay.fill(white)
car(x,y)
    


    pygame.display.update()
    clock.tick()
  

pygame.quit()
quit()
