import pygame
from constantes import *

class Cura(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.assets = {}
        self.assets['cura'] = pygame.image.load('Site/imagens/logo-jogo 3.png')
        self.assets['cura'] = pygame.transform.scale(self.assets['cura'], (16, 16))
        self.imagem = self.assets['cura'].copy()
        self.rect = self.assets['cura'].get_rect()
        self.rect.x = x
        self.rect.y = y
        self.pos = 0
        
    def desenha(self, tela, camera):
        '''
        Desenha a cura na tela
        '''
        pos = (self.rect.x - camera.x, self.rect.y - camera.y)
        self.pos = pos
        tela.blit(self.imagem, pos)