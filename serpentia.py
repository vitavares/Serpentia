import pygame, sys
from pygame.locals import *
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
velocidade = 7
x_controle = velocidade
y_controle = 0
relogio = pygame.time.Clock()
fonte = pygame.font.SysFont('uroob', 30, False, False)

SURFACE = pygame.display.set_mode((largura_tela,altura_tela)) #tamanho da janela
pygame.display.set_caption("serpentia") #identificação

msc_ponto = pygame.mixer.Sound('media/coin.wav')
msc_morte = pygame.mixer.Sound('media/morte.mp3')
msc_fundo = pygame.mixer.music.load('media/fundo.mp3')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

def up_serpentia(list_serpentia):
    for XeY in list_serpentia:
        pygame.draw.rect(SURFACE, (127,255,212), (XeY[0], XeY[1], 20,20))

def restart_game():
    global points, xserpentia, yserpentia, xcoin, ycoin, serpentia_comp, morreu, list_serpentia, head
    points = 0
    xserpentia = int((largura_tela/2)-25)
    yserpentia = int((altura_tela/2)-25)
    xcoin = randint(40, 600)
    ycoin = randint(50, 430)
    serpentia_comp = 5
    morreu = False
    list_serpentia = []
    head = []

morreu = False
while True:
    relogio.tick(30)
    SURFACE.fill((105,89,205))

    for event in pygame.event.get():
        if event.type == QUIT:
            print(points)
            pygame.quit()
            sys.exit()
        if  event.type == KEYDOWN:
            if event.key == K_a and x_controle != velocidade:
                    x_controle = -velocidade
                    y_controle = 0
            if event.key == K_d and x_controle != -velocidade:
                    x_controle = velocidade
                    y_controle = 0
            if event.key == K_w and y_controle != velocidade:
                    y_controle = -velocidade
                    x_controle = 0
            if event.key == K_s and y_controle != -velocidade:
                    y_controle = velocidade
                    x_controle = 0
    xserpentia = xserpentia + x_controle
    yserpentia = yserpentia + y_controle

    serpentia = pygame.draw.rect(SURFACE, ((127,255,212)), (xserpentia, yserpentia, 25, 25))
    coin = pygame.draw.rect(SURFACE, ((218,165,32)), (xcoin, ycoin, 30, 30))

    if serpentia.colliderect(coin):
        if xcoin in list_serpentia or ycoin in list_serpentia:
            xcoin = randint(40, 600)
            ycoin = randint(50, 430)
        points = points+1
        msc_ponto.play()
        serpentia_comp = serpentia_comp + 1
    pontuacao = fonte.render(('coins: {}'.format(points)), False, (0,0,0))

    head = []
    head.append(xserpentia)
    head.append(yserpentia)
    list_serpentia.append(head) #como prender a cobra??

    if list_serpentia.count(head) >1:
        pygame.mixer.music.stop()
        msc_morte.play()
        fonte2 = pygame.font.SysFont('uroob', 30, False, False)
        mensagem = 'Você perdeu !!  Pressione R para jogar novamente =) {}'.format(points)
        msg_morte = fonte2.render(mensagem, False, (0,0,0))
        ret_mensagem = msg_morte.get_rect()
        morreu = True
        SURFACE.fill((255,255,255))
        while morreu:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        restart_game()

            ret_mensagem.center = (largura_tela//2, altura_tela//2)
            SURFACE.blit(msg_morte, ret_mensagem)
            pygame.display.flip()

    if len(list_serpentia) > serpentia_comp:
        del list_serpentia[0]

    up_serpentia(list_serpentia)
    SURFACE.blit(pontuacao, (520,10))

    pygame.display.flip()