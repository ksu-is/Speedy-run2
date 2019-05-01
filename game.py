import pygame

pygame.init()

raceDisplay = pygame.display.set_mode((1000,850))
pygame.display.set_caption('Speedy Run')

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
