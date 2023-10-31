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
        self.assets['inimigo1_pre_ataque'] = pygame.image.load('img/inimigos/inimigo-1-pre-ataque.png')
        self.assets['inimigo1_ataque'] = pygame.image.load('img/inimigos/inimigo-1-atacando.png')

        self.assets['inimigo2_idle'] = pygame.image.load('img/inimigos/inimigo-2-parado.png')
        self.assets['inimigo2_move'] = pygame.image.load('img/inimigos/inimigo-2-andando.png')
        self.assets['inimigo2_pre_ataque'] = pygame.image.load('img/inimigos/inimigo-2-pre-ataque.png')
        self.assets['inimigo2_ataque'] = pygame.image.load('img/inimigos/inimigo-2-atacando.png')

        self.assets['inimigo3_idle'] = pygame.image.load('img/inimigos/inimigo-3-parado.png')
        self.assets['inimigo3_move'] = pygame.image.load('img/inimigos/inimigo-3-andando.png')
        self.assets['inimigo3_ataque'] = pygame.image.load('img/inimigos/inimigo-3-atacando.png')

        self.assets['inimigo4_idle'] = pygame.image.load('img/inimigos/inimigo-4-parado.png')
        self.assets['inimigo4_move'] = pygame.image.load('img/inimigos/inimigo-4-andando.png')
        self.assets['inimigo4_pre_ataque'] = pygame.image.load('img/inimigos/inimigo-4-pre-ataque.png')
        self.assets['inimigo4_ataque'] = pygame.image.load('img/inimigos/inimigo-4-atacando.png')

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

    def update(self):
        '''
        Atualiza a posição do inimigo
        '''
        self.rect.x += self.velocidade_x * self.direcao
        self.estado = 'move'
        self.distancia_percorrida += abs(self.velocidade_x)

        # Se percorreu 3 blocos, muda a direção
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