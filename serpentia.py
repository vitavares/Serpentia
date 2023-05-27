import pygame, sys
from pygame.locals import * # submodulo com constantes e funções

pygame.init()

largura = 640
altura = 480
x = (largura/2)-25
y = (altura/2)-25
SURFACE = pygame.display.set_mode((largura,altura)) #tamanho da janela
pygame.display.set_caption("serpentia") #identificação
relogio = pygame.time.Clock()

while True:
    relogio.tick(60) #frames por segundo
    SURFACE.fill((105,89,205))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    if pygame.key.get_pressed()[K_a]:
        x = x-20
    if pygame.key.get_pressed()[K_d]:
        x = x+20
    if pygame.key.get_pressed()[K_w]:
        y = y-20
    if pygame.key.get_pressed()[K_s]:
        y = y+20
    pygame.draw.rect(SURFACE, (0,0,0), (x, y, 50, 50))
    pygame.display.update()