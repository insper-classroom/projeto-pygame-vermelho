import pygame
from constantes import *

class Telagameover(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        '''
        Inicializa as sprites da tela final
        '''
        self.assets = {}
        self.assets['telagameover'] = pygame.image.load('img/gameover.png')
        self.assets['telagameover'] = pygame.transform.scale(self.assets['telagameover'], (1200, 600))

    def desenha(self, tela):
        '''
        Desenha a tela inicial
        '''
        tela.blit(self.assets['telagameover'], (0, 0))