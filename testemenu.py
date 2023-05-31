import pygame, sys
from pygame.locals import * 

pygame.init()

altura_tela = 640
largura_tela = 480

SURFACE = pygame.display.set_mode((altura_tela, largura_tela))
pygame.display.set_caption("menu")

run = True
while run:
    SURFACE.fill((105,89,205))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
