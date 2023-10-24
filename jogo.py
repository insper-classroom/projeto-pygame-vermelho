import pygame
from constantes import *

def inicializa():
    pygame.init()
    tela = pygame.display.set_mode((800, 600), 0, 0)
    pygame.display.set_caption('Jogo')

    return tela

def eventos():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False

    return True

def atualiza(tela):
    tela.fill((0, 0, 0))
    pygame.display.update()

def game_loop():
    tela = inicializa()

    while eventos():
        atualiza(tela)

    pygame.quit()

game_loop()