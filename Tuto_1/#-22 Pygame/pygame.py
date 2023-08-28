import pygame
## Creer en 2000 
## peut faire du 3D, 2D

pygame.init()
screen = pygame.display.set_mode((640,480))

launched = True

while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched