#import pygame
import pygame
#closing game
import sys
#initialize game
pygame.init()

Width=1000
Height=850


# Open a window
size = (Width, Height)
screengame = pygame.display.set_mode(size)

# Set title to the window
pygame.display.set_caption("Speedy")

race=False

clock = pygame.time.Clock()
background_image = pygame.image.load("image1.jpg").convert()
carimage1 = pygame.image.load('car.png')

#define car
    
while(race==False):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True
            sys.exit()

    screengame.blit(background_image, [0, 0])

def car1(x,y):
    screengame.blit(carimage1,(450,100))
    pygame.display.flip()
    carimage1(450,100)
    clock.tick()
