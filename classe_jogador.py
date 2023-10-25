import pygame
from constantes import *

class Jogador(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.x = x
        self.y = y
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
        for i in range(len(self.assets['idle'])):
            tela.blit(self.assets['idle'][i], (self.x, self.y))