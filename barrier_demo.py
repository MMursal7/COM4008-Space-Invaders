import pygame
from barrier import Barrier

pygame.init()
screen = pygame.display.set_mode([500, 500])
clock = pygame.time.Clock()

ones = [ Barrier(52, 380), Barrier(164, 380), Barrier(276, 380), Barrier(388, 380) ]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill([0, 0, 0])
    for one in ones :
        if one.alive:
            pygame.draw.rect(screen, (0, 255, 0), one.rect)

    pygame.display.flip()
    clock.tick(90)

pygame.quit()
