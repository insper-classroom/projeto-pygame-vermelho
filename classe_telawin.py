import pygame
from constantes import *

class TelaWin(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        '''
        Inicializa as sprites da tela final
        '''
        self.assets = {}
        self.assets['telawin'] = pygame.image.load('img/Win.png')
        self.assets['telawin'] = pygame.transform.scale(self.assets['telawin'], (1200, 600))

    def desenha(self, tela):
        '''
        Desenha a tela inicial
        '''
        tela.blit(self.assets['telawin'], (0, 0))