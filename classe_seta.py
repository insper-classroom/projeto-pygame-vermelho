import pygame
from constantes import *

class Setas(pygame.sprite.Sprite):
    def __init__(self, x, y):
        '''
        Inicializa o personagem
        '''
        pygame.sprite.Sprite.__init__(self)
        self.assets = {}
        self.assets['seta'] = pygame.image.load('img/arrows-png.webp')
        self.assets['seta'] = pygame.transform.scale(self.assets['seta'], (64, 64))

        self.imagem = self.assets['seta'].copy()
        self.rect = self.assets['seta'].get_rect()
        self.rect.x = x
        self.rect.y = y
        self.pos = 0


    def desenha(self, tela, camera):
        '''
        Desenha a seta na tela
        '''
        #Desenha a seta e angula ela
        self.imagem = pygame.transform.rotate(self.assets['seta'], 90)
        pos = (self.rect.x - camera.x, self.rect.y - camera.y)
        self.pos = pos
        tela.blit(self.imagem, pos)