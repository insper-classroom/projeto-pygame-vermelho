import pygame
from constantes import *

class Cura(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.assets = {}
        self.assets['cura'] = pygame.image.load('img/Abertura.png')
        self.assets['cura'] = pygame.transform.scale(self.assets['cura'], (16, 16))
        self.imagem = self.assets['cura'].copy()
        self.rect = self.assets['cura'].get_rect()
        self.rect.x = x
        self.rect.y = y
        self.pos = 0
        self.flip = False
        self.timer = 0
        self.flip_timer = 10

    def rotacao(self):
        '''
        Rotaciona a cura
        '''
        self.timer += 1
        if self.timer >= self.flip_timer:
            self.timer = 0
            self.flip = not self.flip
            self.imagem = pygame.transform.flip(self.imagem, True, False)
            self.timer = 0
        
    def desenha(self, tela, camera):
        '''
        Desenha a cura na tela
        '''
        pos = (self.rect.x - camera.x, self.rect.y - camera.y)
        self.pos = pos
        tela.blit(self.imagem, pos)