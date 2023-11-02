import pygame
from constantes import *

class Telainicial(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        '''
        Inicializa as sprites da tela inicial
        '''
        self.assets = {}
        self.assets['telainicial'] = pygame.image.load('img/Abertura.png')
        self.assets['telainicial'] = pygame.transform.scale(self.assets['telainicial'], (1200, 600))

    def desenha(self, tela):
        '''
        Desenha a tela inicial
        '''
        tela.blit(self.assets['telainicial'], (0, 0))
        tela.blit(pygame.font.SysFont('arial', 50).render('Aperte espaço para prosseguir', True, (255, 255, 255)), (370, 540))