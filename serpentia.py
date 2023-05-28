import pygame, sys
from pygame.locals import * # submodulo com constantes e funções
from random import randint

pygame.init()

points = 0
largura_tela = 640
altura_tela = 480
xserpentia = int((largura_tela/2)-25)
yserpentia = int((altura_tela/2)-25)
xcoin = randint(40, 600)
ycoin = randint(50, 430)
list_serpentia = []
serpentia_comp = 5
velocidade = 5
x_controle = velocidade
y_controle = 0

fonte = pygame.font.SysFont('uroob', 30, False, False)
msc_fundo = pygame.mixer.music.load('media/fundo.mp3')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)
msc_ponto = pygame.mixer.Sound('media/coin.wav')

SURFACE = pygame.display.set_mode((largura_tela,altura_tela)) #tamanho da janela
pygame.display.set_caption("serpentia") #identificação
relogio = pygame.time.Clock()

def up_serpentia(list_serpentia):
    for XeY in list_serpentia:
        pygame.draw.rect(SURFACE, (127,255,212), (XeY[0], XeY[1], 30,30))

while True:
    relogio.tick(60) #frames por segundo
    SURFACE.fill((105,89,205))
    mensagem = fonte.render(('coins: {}'.format(points)), False, (0,0,0))

    for event in pygame.event.get():
        if event.type == QUIT:
            print(points)
            pygame.quit()
            sys.exit()
        if  event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0
            if event.key == K_d:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = -velocidade
                    x_controle = 0
            if event.key == K_s:
                if y_controle == -velocidade:
                    pass
                else:
                    y_controle = velocidade
                    x_controle = 0

    xserpentia = xserpentia + x_controle
    yserpentia = yserpentia + y_controle

    serpentia = pygame.draw.rect(SURFACE, ((127,255,212)), (xserpentia, yserpentia, 30, 30))
    coin = pygame.draw.rect(SURFACE, ((218,165,32)), (xcoin, ycoin, 30, 30))

    if serpentia.colliderect(coin):
        xcoin = randint(40, 600)
        ycoin = randint(50, 430)
        points = points+1
        msc_ponto.play()
        serpentia_comp = serpentia_comp + 1

    
    head = []
    head.append(xserpentia)
    head.append(yserpentia)
    list_serpentia.append(head) #como prender a cobra??


    if len(list_serpentia) > serpentia_comp:
        del list_serpentia[0]

    up_serpentia(list_serpentia)
    SURFACE.blit(mensagem, (520,10))

    pygame.display.update()