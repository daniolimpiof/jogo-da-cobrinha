import pygame
from pygame.locals import *
import random

pygame.init()

# variaveis
ESQUERDA = K_LEFT
DIREITA = K_RIGHT
CIMA = K_UP
BAIXO = K_DOWN

TAMANHO_DO_PASSO = 10

# tela
tamanho_da_tela = (660, 600)
tela = pygame.display.set_mode(tamanho_da_tela)
pygame.display.set_caption("Jogo da Cobrinha")

# cobra
posicoes_da_cobra = [(300, 300)]
superficie_da_cobra = pygame.surface.Surface((10, 10))
superficie_da_cobra.fill((255, 255, 255))
direcao_da_cobra = DIREITA


# maçã
def gerar_posicao_da_maca():
    x = random.randint(0, tamanho_da_tela[0])
    y = random.randint(0, tamanho_da_tela[1])
    x = x // TAMANHO_DO_PASSO * TAMANHO_DO_PASSO
    y = y // TAMANHO_DO_PASSO * TAMANHO_DO_PASSO
    return (x, y)


posicao_da_maca = gerar_posicao_da_maca()
superficie_da_maca = pygame.surface.Surface((10, 10))
superficie_da_maca.fill((255, 0, 0))


def colisao_com_maca(posicao1, posicao2):
    return posicao1 == posicao2


def colisao_com_parede(posicao_da_cobra):
    if (
        0 <= posicao_da_cobra[0] < tamanho_da_tela[0]
        and 0 <= posicao_da_cobra[1] < tamanho_da_tela[1]
    ):
        return False
    else:
        return True


while True:
    # limitar tempo de movimento
    pygame.time.Clock().tick(10)

    tela.fill((0, 0, 0))

    # verifica os eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # verifica se apertou alguma tecla
        if event.type == pygame.KEYDOWN:
            if event.key == ESQUERDA:
                direcao_da_cobra = ESQUERDA
            if event.key == DIREITA:
                direcao_da_cobra = DIREITA
            if event.key == CIMA:
                direcao_da_cobra = CIMA
            if event.key == BAIXO:
                direcao_da_cobra = BAIXO

    # desenha a cobra
    for posicao in posicoes_da_cobra:
        tela.blit(superficie_da_cobra, posicao)
    # tamanho da cobra
    tamanho_da_cobrinha = len(posicoes_da_cobra) - 1

    # verifica colisão com parede
    if colisao_com_parede(posicoes_da_cobra[0]):
        pygame.quit()
        quit()

    # verifica colisão com maçã
    if colisao_com_maca(posicoes_da_cobra[0], posicao_da_maca):
        posicao_da_maca = gerar_posicao_da_maca()
        posicoes_da_cobra.append((0, 0))

    # aumenta o tamanho da cobra
    for i in range(tamanho_da_cobrinha, 0, -1):
        posicoes_da_cobra[i] = posicoes_da_cobra[i - 1]

    if colisao_com_maca(posicoes_da_cobra[0], posicao_da_maca):
        posicoes_da_cobra.append(posicoes_da_cobra[tamanho_da_cobrinha])
        posicao_da_maca = gerar_posicao_da_maca()

    # desenha a maçã
    tela.blit(superficie_da_maca, posicao_da_maca)

    if direcao_da_cobra == DIREITA:
        posicoes_da_cobra[0] = (
            posicoes_da_cobra[0][0] + TAMANHO_DO_PASSO,
            posicoes_da_cobra[0][1],
        )
    if direcao_da_cobra == ESQUERDA:
        posicoes_da_cobra[0] = (
            posicoes_da_cobra[0][0] - TAMANHO_DO_PASSO,
            posicoes_da_cobra[0][1],
        )
    if direcao_da_cobra == CIMA:
        posicoes_da_cobra[0] = (
            posicoes_da_cobra[0][0],
            posicoes_da_cobra[0][1] - TAMANHO_DO_PASSO,
        )
    if direcao_da_cobra == BAIXO:
        posicoes_da_cobra[0] = (
            posicoes_da_cobra[0][0],
            posicoes_da_cobra[0][1] + TAMANHO_DO_PASSO,
        )

    pygame.display.update()
