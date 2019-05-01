#import pygame
import pygame

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

while(race==False):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True

    screengame.blit(background_image, [0, 0])

    pygame.display.flip()
    clock.tick()
