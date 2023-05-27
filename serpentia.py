import pygame, sys
from pygame.locals import * # submodulo com constantes e funções
from random import randint
pygame.init()

points = 0
largura = 640
altura = 480
comprimento = 50
x = (largura/2)-25
y = (altura/2)-25
x_2 = randint(40, 600)
y_2 = randint(50, 430)
fonte = pygame.font.SysFont('uroob', 30, False, False)


SURFACE = pygame.display.set_mode((largura,altura)) #tamanho da janela
pygame.display.set_caption("serpentia") #identificação
relogio = pygame.time.Clock()

while True:
    relogio.tick(60) #frames por segundo
    SURFACE.fill((105,89,205))
    mensagem = fonte.render(('Pontos: {}'.format(points)), True, (0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            print(points)
            pygame.quit()
            sys.exit()

    if pygame.key.get_pressed()[K_a or K_LEFT]:
        x = x-5
    if pygame.key.get_pressed()[K_d or K_RIGHT]:
        x = x+5
    if pygame.key.get_pressed()[(K_w) or (K_UP)]:
        y = y-5
    if pygame.key.get_pressed()[K_s or K_DOWN]:
        y = y+5

    ret_1 = pygame.draw.rect(SURFACE, (0,0,0), (x, y, comprimento, 50))
    ret_2 = pygame.draw.rect(SURFACE, (0,0,200), (x_2, y_2, 50, 50))
    if ret_1.colliderect(ret_2):
        x_2 = randint(40, 600)
        y_2 = randint(50, 430)
        points = points+1
        comprimento = comprimento + 50
    SURFACE.blit(mensagem, (520,10))
    pygame.display.update()