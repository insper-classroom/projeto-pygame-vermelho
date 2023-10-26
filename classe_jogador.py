import pygame
from constantes import *

class Jogador(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.assets = {}
        self.assets['jogador_idle'] = pygame.image.load('img/personagem-principal-parado.png')
        self.assets['jogador_move'] = pygame.image.load('img/personagem-pricipal-andando.png')
        self.assets['jogador_jump'] = pygame.image.load('img/personagem-principal-pulando.png')
        self.assets['jogador_morte'] = pygame.image.load('img/personagem-principal-morto.png')
        self.assets['jogador_idle'] = pygame.transform.scale_by(self.assets['jogador_idle'],1.5)
        self.assets['jogador_move'] = pygame.transform.scale_by(self.assets['jogador_move'],1.5)
        self.assets['jogador_jump'] = pygame.transform.scale_by(self.assets['jogador_jump'],1.5)
        self.assets['jogador_morte'] = pygame.transform.scale_by(self.assets['jogador_morte'],1.5)

        self.rect = self.assets['jogador_idle'].get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocidade_x = 0
        self.velocidade_y = 0
        self.estado = 'jogador_idle'
        self.state = STILL
    
    def desenha(self, tela):
        if self.velocidade_x == 0 and self.velocidade_y == 0:
            self.set_estado('jogador_idle')
        elif self.velocidade_x > 0 and self.velocidade_y == 0:
            self.set_estado('jogador_move')
        tela.blit(self.assets[self.estado], (self.rect.x, self.rect.y))

    # Método que faz o personagem pular
    def jump(self):
        # Só pode pular se ainda não estiver pulando ou caindo
        if self.state == STILL:
            self.velocidade_y -= JUMP_SIZE
            self.state = JUMPING

    def set_estado(self, estado):
        if self.estado != estado:
            self.estado = estado
            self.frame_atual = 0
    
    # Metodo que atualiza a posição do personagem
    def update(self):
        self.velocidade_y += GRAVITY
        # Atualiza o estado para caindo
        if self.velocidade_y > 0:
            self.state = FALLING
        self.rect.y += self.velocidade_y
        # Se bater no chão, para de cair
        if self.rect.bottom > GROUND:
            # Reposiciona para a posição do chão
            self.rect.bottom = GROUND
            # Para de cair
            self.velocidade_y = 0
            # Atualiza o estado para parado
            self.state = STILL
        
        self.rect.x += self.velocidade_x
        self.rect.y += self.velocidade_y