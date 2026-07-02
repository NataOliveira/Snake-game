import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()
pygame.display.set_caption('Snake')

largura = 640
altura = 480
x_cobra = (largura/2) - 15
y_cobra = (altura/2) - 15
x_controle = 20
y_controle = 0
x_comida = randint(40, (largura- 40))
y_comida = randint(40, (altura- 40))
pontos = 0
morreu = False
velocidade = 10
relogio = pygame.time.Clock()
take_coin = pygame.mixer.Sound('take.mp3')
pygame.mixer.music.load('music.wav')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)
fonte = pygame.font.SysFont('arial', 30, True, False)
tela = pygame.display.set_mode((largura, altura))
lista_cobra = []
tamanho_cobra = 1

def desenhar_cobra(lista_cobra_function):
    for XeY in lista_cobra_function:
        pygame.draw.rect(tela, (0, 0, 0), (XeY[0], XeY[1], 25, 25),border_radius=6)

def reiniciar_jogo():
    global pontos, tamanho_cobra,x_cobra, y_cobra,lista_cobra,lista_cabeca, x_comida, y_comida, morreu, velocidade
    pontos = 0
    tamanho_cobra = 1
    x_cobra = (largura/2) - 15
    y_cobra = (altura/2) - 15
    lista_cobra = []
    lista_cabeca = []
    x_comida = randint(30, largura)
    y_comida = randint(30, altura)
    velocidade = 10
    morreu = False

while True:
    tela.fill((0, 100, 0))
    relogio.tick(velocidade)
    mensagem = f'Pontos: {pontos}'
    texto_pontos = fonte.render(mensagem, True, (255, 255, 255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle  = -velocidade
                    y_controle = 0
            if event.key == K_RIGHT:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            if event.key == K_UP:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = -velocidade
                    x_controle = 0
            if event.key == K_DOWN:
                if y_controle == -velocidade:
                    pass
                else:
                    y_controle = velocidade
                    x_controle = 0

    x_cobra = x_cobra + x_controle
    y_cobra = y_cobra + y_controle

    # atualiza a posição da cabeça na lista antes de desenhar
    lista_cabeca = [x_cobra, y_cobra]
    lista_cobra.append(lista_cabeca)

    if lista_cobra.count(lista_cabeca) > 1:
        fonte2 = pygame.font.SysFont('arial', 20, True, False)
        mensagem = 'Gamer Over, press R to try again'
        texto_formatado = fonte2.render(mensagem, True, (255, 255, 255))
        ret_texto = texto_formatado.get_rect()
        morreu = True

        while morreu:
            tela.fill((10, 10, 10))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        print('aqui')
                        reiniciar_jogo()

            ret_texto.center = (largura//2, altura//2)
            tela.blit(texto_formatado,ret_texto)
            pygame.display.update()

    if x_cobra > largura:
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = largura
    if y_cobra > altura:
        y_cobra = 0
    if y_cobra < 0:
        y_cobra = altura

    # remove o rabo se não cresceu
    if len(lista_cobra) > tamanho_cobra:
        del lista_cobra[0]

    tela.blit(texto_pontos, (460, 30))
    comida = pygame.draw.circle(tela, (200, 20, 20), (x_comida + 10, y_comida + 10), 10)
    pygame.draw.rect(tela, (0, 150, 0), (x_comida + 8, y_comida - 4, 4, 6))


    # desenha o corpo inteiro
    desenhar_cobra(lista_cobra)
    # desenha os olhos

    if lista_cobra:
        x_cabeca, y_cabeca = lista_cobra[-1]
        pygame.draw.circle(tela, (255, 255, 255), (x_cabeca + 5, y_cabeca + 5), 2)
        pygame.draw.circle(tela, (255, 255, 255), (x_cabeca + 15, y_cabeca + 5), 2)


    cobra = pygame.Rect(x_cobra, y_cobra, 25, 25)
    #ação de comer a comida
    if cobra.colliderect(comida):
        print('comeu')
        x_comida = randint(30, largura)
        y_comida = randint(30, altura)
        pontos += 1
        velocidade += 0.5
        tamanho_cobra += 1
        take_coin.play()

    pygame.display.update()


