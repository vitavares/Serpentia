import pygame, sys
from pygame.locals import *

pygame.init()
SURFACE = pygame.display.set_mode((300,300))
pygame.display.set_caption("caption")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()