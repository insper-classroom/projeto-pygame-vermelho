import pygame

def inicializa():
    pygame.init()
    tela = pygame.display.set_mode((800, 600), 0, 0)
    pygame.display.set_caption('Jogo')