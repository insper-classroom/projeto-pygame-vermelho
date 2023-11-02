import pygame
from constantes import *

class Inimigo(pygame.sprite.Sprite):
    def __init__(self, x , y, tipo):
        pygame.sprite.Sprite.__init__(self)
        '''
        Inicializa as sprites do inimigo
        '''
        self.assets = {}
        self.assets['inimigo1_idle'] = pygame.image.load('img/inimigos/inimigo-1-parado.png')
        self.assets['inimigo1_move'] = pygame.image.load('img/inimigos/inimigo-1-andando.png')

        self.assets['inimigo2_idle'] = pygame.image.load('img/inimigos/inimigo-2-parado.png')
        self.assets['inimigo2_move'] = pygame.image.load('img/inimigos/inimigo-2-andando.png')

        self.assets['inimigo3_idle'] = pygame.image.load('img/inimigos/inimigo-3-parado.png')
        self.assets['inimigo3_move'] = pygame.image.load('img/inimigos/inimigo-3-andando.png')

        self.assets['inimigo4_idle'] = pygame.image.load('img/inimigos/inimigo-4-parado.png')
        self.assets['inimigo4_move'] = pygame.image.load('img/inimigos/inimigo-4-andando.png')

        self.assets['chefe_idle'] = pygame.image.load('img/inimigos/inimigo-5-parado.png')
        self.assets['chefe_move'] = pygame.image.load('img/inimigos/inimigo-5-andando.png')

        self.rect = self.assets['inimigo1_idle'].get_rect()
        self.tipo = tipo
        self.rect.x = x
        self.rect.y = y
        self.estado = 'idle'
        self.velocidade_x = 1  # Velocidade do movimento
        self.distancia_percorrida = 0
        self.direcao = 1  # 1 para direita, -1 para esquerda
        self.flip = False
        self.pos = 0
        self.tipo = tipo

        if self.tipo == 'chefe':
            self.vida = 3
        else:
            self.vida = 1

        self.chefe = False


    def update(self):
        '''
        Atualiza a posição do inimigo
        '''
        self.rect.x += self.velocidade_x * self.direcao
        self.estado = 'move'
        self.distancia_percorrida += abs(self.velocidade_x)

        # Se percorreu 3 blocos, muda a direção
        if self.tipo == 'chefe':
            if self.distancia_percorrida >= 20 * 32:
                self.direcao *= -1
                self.distancia_percorrida = 0
        else:
            if self.distancia_percorrida >= 3 * 32:
                self.direcao *= -1
                self.distancia_percorrida = 0

        # Verifica a direção do movimento e flipa a sprite se estiver indo para a esquerda
        if self.direcao < 0 and not self.flip:
            self.assets[f'{self.tipo}_move'] = pygame.transform.flip(self.assets[f'{self.tipo}_move'], True, False)
            self.flip = True  # Marca a sprite como flipada
        
        elif self.direcao > 0 and self.flip:
            self.assets[f'{self.tipo}_move'] = pygame.transform.flip(self.assets[f'{self.tipo}_move'], True, False)
            self.flip = False  # Marca a sprite como não flipada

    def desenha(self, tela, camera):
        '''
        Desenha o inimigo na tela
        '''
        pos = (self.rect.x - camera.x, self.rect.y - camera.y)
        self.pos = pos
        tela.blit(self.assets[f'{self.tipo}_{self.estado}'], pos)
        tela.blit(pygame.font.SysFont('arial', 15).render('x' * (self.vida), True, (255, 0, 0)), (pos[0]+7, pos[1] + 28))