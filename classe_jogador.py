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
        self.assets['jogador_idle'] = pygame.transform.scale_by(self.assets['jogador_idle'],1)
        self.assets['jogador_move'] = pygame.transform.scale_by(self.assets['jogador_move'],1)
        self.assets['jogador_jump'] = pygame.transform.scale_by(self.assets['jogador_jump'],1)
        self.assets['jogador_morte'] = pygame.transform.scale_by(self.assets['jogador_morte'],1)

        self.rect = self.assets['jogador_idle'].get_rect()
        self.rect.x = x
        self.rect.y = y
        self.hitbox = pygame.Rect(self.rect.x, self.rect.y, 32, 30)
        self.velocidade_x = 0
        self.velocidade_y = 0
        self.estado = 'jogador_idle'
        self.state = STILL
        self.moving_right = False
        self.moving_left = False
    
    def desenha(self, tela):
        #Desenha o personagem
        pygame.draw.rect(tela, (255, 0, 0), (self.rect.x, self.rect.y, self.rect.width, self.rect.height), 1)
        pygame.draw.rect(tela, (255, 255, 0), (self.hitbox.x, self.hitbox.y, self.hitbox.width, self.hitbox.height), 1)
        tela.blit(self.assets[self.estado], (self.hitbox.x, self.hitbox.y))
        tela.blit(self.assets[self.estado], (self.rect.x, self.rect.y))

    def jump(self):
        # Só pode pular se ainda não estiver pulando ou caindo
        if self.state == STILL and self.velocidade_y == 0.5:
            self.velocidade_y -= 10
            self.state = JUMPING

    def set_estado(self, estado):
        # Só altera o estado se for diferente do atual
        if self.estado != estado:
            self.estado = estado
    
    # Metodo que atualiza a posição do personagem
    def update(self, tiles):
        for tile in tiles:
            if self.hitbox.colliderect(tile):
                if self.velocidade_y < 0.6 and self.velocidade_y > -9: # Colisão com o teto
                    self.velocidade_y = 0
                elif self.velocidade_x > 0: # Colisão com a direita
                    self.rect.right = tile.left
                elif self.velocidade_x < 0: # Colisão com a esquerda
                    self.rect.left = tile.right

            #Colisão com o chão
            elif self.rect.colliderect(tile):
                if self.velocidade_y > 0:  # Colisão abaixo
                    self.rect.bottom = tile.top
                    self.velocidade_y = 0
                    self.state = STILL
        # Gravidade
        self.velocidade_y += 0.5
        self.state = STILL

        # Atualiza a posição do personagem
        if self.velocidade_y < 0.5 or self.velocidade_y > 0.5:
            self.set_estado('jogador_jump')
        elif self.moving_right:
            self.velocidade_x = 2
            self.set_estado('jogador_move')
        elif self.moving_left:
            self.velocidade_x = -2
            self.set_estado('jogador_move')
        else:
            self.velocidade_x = 0
            self.set_estado('jogador_idle')

        self.rect.y += self.velocidade_y
        self.rect.x += self.velocidade_x
        self.hitbox.x = self.rect.x
        self.hitbox.y = self.rect.y