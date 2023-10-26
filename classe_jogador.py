import pygame
from constantes import *

class Jogador(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocidade_x = 0
        self.velocidade_y = 0
        self.estado = 'idle'
        self.frame_atual = 0
        self.contador_ticks = 0
        self.delay_animacao = 5
    
        self.assets = {}
        self.assets['jogador_idle'] = pygame.image.load('img/idle_personagem.jpg')
        self.assets['jogador_move'] = pygame.image.load('img/mov_personagem.jpg')
        self.assets['jogador_jump'] = pygame.image.load('img/jump_personagem.jpg')
        self.assets['jogador_dano'] = pygame.image.load('img/dano_personagem.jpg')
        self.assets['jogador_attack'] = pygame.image.load('img/attk1_personagem.jpg')
        self.assets['jogador_attack2'] = pygame.image.load('img/attk2_personagem.jpg')
        self.assets['jogador_morte'] = pygame.image.load('img/morte_personagem.jpg')
        self.assets['idle'] = self.load_spritesheet(self.assets['jogador_idle'], 1, 6)
        self.assets['move'] = self.load_spritesheet(self.assets['jogador_move'], 1, 7)
        self.assets['jump'] = self.load_spritesheet(self.assets['jogador_jump'], 1, 8)
        self.assets['dano'] = self.load_spritesheet(self.assets['jogador_dano'], 1, 2)
        self.assets['attack'] = self.load_spritesheet(self.assets['jogador_attack'], 1, 5)
        self.assets['attack2'] = self.load_spritesheet(self.assets['jogador_attack2'], 1, 5)
        self.assets['morte'] = self.load_spritesheet(self.assets['jogador_morte'], 1, 4)

    def load_spritesheet(self, sprite_sheet, rows, columns):
        sprite_width = sprite_sheet.get_width()//columns
        sprite_height = sprite_sheet.get_height()//rows
        sprites = []
        for i in range(rows):
            for j in range(columns):
                sprite = sprite_sheet.subsurface(j*sprite_width, i*sprite_height, sprite_width, sprite_height)
                sprites.append(sprite)
        return sprites
    
    def desenha(self, tela):
        if self.velocidade_x == 0 and self.velocidade_y == 0:
            self.set_estado('idle')
        elif self.velocidade_x > 0 and self.velocidade_y == 0:
            self.set_estado('move')
        elif self.velocidade_y < 0:
            self.set_estado('jump')
        tela.blit(self.assets[self.estado][self.frame_atual], (self.x, self.y))

    def mover(self):
        self.x += self.velocidade_x
        self.y += self.velocidade_y

    def set_estado(self, estado):
        if self.estado != estado:
            self.estado = estado
            self.frame_atual = 0
    
    def set_velocidade_x(self, velocidade_x):
        self.velocidade_x = velocidade_x

    def set_velocidade_y(self, velocidade_y):
        self.velocidade_y = velocidade_y

    def atualizar_animacao(self):
        self.contador_ticks += 1
        if self.contador_ticks >= self.delay_animacao:
            self.contador_ticks = 0
            self.frame_atual += 1
            if self.frame_atual >= len(self.assets[self.estado]):
                self.frame_atual = 0