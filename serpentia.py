import pygame, sys
from pygame.locals import * # submodulo com constantes e funções
from random import randint
pygame.init()

points = 0
largura_tela = 640
altura_tela = 480
comprimento = 50
x = int((largura_tela/2)-25)
y = int((altura_tela/2)-25)
x_2 = randint(40, 600)
y_2 = randint(50, 430)
fonte = pygame.font.SysFont('uroob', 30, False, False)
msc_fundo = pygame.mixer.music.load('media/fundo.mp3')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)
msc_ponto = pygame.mixer.Sound('media/coin.wav')
SURFACE = pygame.display.set_mode((largura_tela,altura_tela)) #tamanho da janela
pygame.display.set_caption("serpentia") #identificação
relogio = pygame.time.Clock()

while True:
    relogio.tick(60) #frames por segundo
    SURFACE.fill((105,89,205))
    mensagem = fonte.render(('Pontos: {}'.format(points)), False, (0,0,0))
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

    serpentia = pygame.draw.rect(SURFACE, ((127,255,212)), (x, y, comprimento, 50))
    coin = pygame.draw.rect(SURFACE, ((218,165,32)), (x_2, y_2, 50, 50))
    if serpentia.colliderect(coin):
        x_2 = randint(40, 600)
        y_2 = randint(50, 430)
        points = points+1
        comprimento = comprimento + 50
        msc_ponto.play()
    SURFACE.blit(mensagem, (520,10))
    pygame.display.update()