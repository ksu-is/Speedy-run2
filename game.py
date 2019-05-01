# import pygame from library
import pygame

pygame.init()
# size and set the main display of the game.
raceDisplay = pygame.display.set_mode((width,height))
pygame.display.set_caption('Speedy Run')
# This is for frame per second of the game. If we put high value in the () The game goes more smoothly.
clock = pygame.time.Clock()

speed = False

while not speed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            speed = True

        print(event)

    pygame.display.update()
    clock.tick()
    
pygame.quit()
quit()
