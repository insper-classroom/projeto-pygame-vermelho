import pygame
from constantes import *

class Jogador(pygame.sprite.Sprite):
    def __init__(self, x, y, grupo_inimigos):
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
        self.velocidade_x = 0
        self.velocidade_y = 0
        self.estado = 'jogador_idle'
        self.state = STILL
        self.moving_right = False
        self.moving_left = False
        self.flip = False
        self.vida = 3
        self.timer = 0
        self.contador = 0
        self.grupo_inimigos = grupo_inimigos
    
    def desenha(self, tela):
        '''
        Desenha o personagem na tela
        '''
        jogador_imagem = self.assets[self.estado].copy()
        #Desenha o personagem
        if self.flip:
            jogador_imagem = pygame.transform.flip(jogador_imagem, True, False)
        if self.timer > 0 and self.timer % 30 < 15:
            return
        
        tela.blit(jogador_imagem, (self.rect.x, self.rect.y))
        tela.blit(pygame.font.SysFont('arial', 30).render('Vidas: ' + str(self.vida), True, (255, 255, 255)), (0, 0))

    def jump(self):
        '''
        Pulo do personagem
        '''
        # Só pode pular se ainda não estiver pulando ou caindo
        if self.state == STILL:
            self.velocidade_y -= 10
            self.state = JUMPING

    def set_estado(self, estado):
        '''
        Muda o estado do personagem
        '''
        # Só altera o estado se for diferente do atual
        if self.estado != estado:
            self.estado = estado


    # Metodo que atualiza a posição do personagem
    def update(self, tiles):
        '''
        Atualiza a posição do personagem e Gravidade
        '''
        # Gravidade
        self.velocidade_y += 0.5

        # Atualiza a animação do personagem e movimentação
        if self.velocidade_y < 0.5 or self.velocidade_y > 0.5:
            self.set_estado('jogador_jump')
            self.state = JUMPING  
        elif self.moving_right:
            self.velocidade_x = 1.8
            self.set_estado('jogador_move')
            self.state = STILL
        elif self.moving_left:
            self.velocidade_x = -1.8
            self.set_estado('jogador_move')
            self.state = STILL
        else:
            self.velocidade_x = 0
            self.set_estado('jogador_idle')
            self.state = STILL

        # Atualiza a posição y do personagem
        self.rect.y += self.velocidade_y

        '''
        Colisão com o mapa
        '''
        for tile in tiles: # Colisão vertical
            if self.rect.colliderect(tile):
                if self.velocidade_y > 0: # Colisão do chão
                    self.rect.bottom = tile.top
                    self.velocidade_y = 0
                elif self.velocidade_y < 0: # Colisão do teto
                    self.rect.top = tile.bottom
                    self.velocidade_y = 0

        # Atualiza a posição x do personagem
        self.rect.x += self.velocidade_x

        for tile in tiles: # Colisão horizontal
            if self.rect.colliderect(tile):
                if self.velocidade_x > 0: # Colisão com a direita
                    self.rect.right = tile.left
                elif self.velocidade_x < 0: # Colisão com a esquerda
                    self.rect.left = tile.right

    