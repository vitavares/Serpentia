import pygame, sys
from pygame.locals import * # submodulo com constantes e funções

pygame.init()

largura = 640
altura = 480
x = 295
y = 0
SURFACE = pygame.display.set_mode((largura,altura)) #tamanho da janela
pygame.display.set_caption("serpentia") #identificação
relogio = pygame.time.Clock()

while True:
    relogio.tick(50) #frames por segundo
    SURFACE.fill((105,89,205))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.draw.rect(SURFACE, (0,0,0), (x, y, 50, 50))
    if y >= altura:
        y = 0
    y = y+1
    pygame.display.update()