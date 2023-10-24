import pygame
import math
from constantes import *

class Jogo:
    def __init__(self):
        pygame.init()
        self.tela = pygame.display.set_mode((1200, 600), 0, 0)
        pygame.display.set_caption('Jogo')

        self.assets = {}
        self.assets['fundo'] = pygame.image.load('img/Backgroud.jpg')
        self.assets['fundo_agua'] = pygame.image.load('img/Background_agua.png')
        self.assets['sprite_idle'] = pygame.image.load('img/idle_personagem.jpg')
        self.assets['sprite_move'] = pygame.image.load('img/mov_personagem.jpg')
        self.assets['sprite_jump'] = pygame.image.load('img/jump_personagem.jpg')
        self.assets['sprite_dano'] = pygame.image.load('img/dano_personagem.jpg')
        self.assets['sprite_attack'] = pygame.image.load('img/attk1_personagem.jpg')
        self.assets['sprite_attack2'] = pygame.image.load('img/attk2_personagem.jpg')
        self.assets['sprite_morte'] = pygame.image.load('img/morte_personagem.jpg')
        self.assets['idle'] = self.load_spritesheet(self.assets['sprite_idle'], 1, 6)
        self.assets['move'] = self.load_spritesheet(self.assets['sprite_move'], 1, 7)
        self.assets['jump'] = self.load_spritesheet(self.assets['sprite_jump'], 1, 8)
        self.assets['dano'] = self.load_spritesheet(self.assets['sprite_dano'], 1, 2)
        self.assets['attack'] = self.load_spritesheet(self.assets['sprite_attack'], 1, 5)
        self.assets['attack2'] = self.load_spritesheet(self.assets['sprite_attack2'], 1, 5)
        self.assets['morte'] = self.load_spritesheet(self.assets['sprite_morte'], 1, 4)

        self.state = {}
        self.state['scroll'] = 0
        
    def load_spritesheet(self, sprite_sheet, rows, columns):
        sprite_width = sprite_sheet.get_width()//columns
        sprite_height = sprite_sheet.get_height()//rows
        sprites = []
        for i in range(rows):
            for j in range(columns):
                sprite = sprite_sheet.subsurface(j*sprite_width, i*sprite_height, sprite_width, sprite_height)
                sprites.append(sprite)
        return sprites
    
    def eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        return True
    
    def desenha(self):
        self.tela.fill(PRETO)
        bg_width = self.assets['fundo'].get_width()
        tiles = math.ceil(1200/bg_width) + 1
        for i in range(0, tiles):
            self.tela.blit(self.assets['fundo'], (i*bg_width + self.state['scroll'], 0))
        self.state['scroll'] -= 1
        if abs(self.state['scroll']) > bg_width:
            self.state['scroll'] = 0
        
        bg_width_agua = self.assets['fundo_agua'].get_width()
        tiles_agua = math.ceil(1200/bg_width_agua) + 1
        for i in range(0, tiles_agua):
            self.tela.blit(self.assets['fundo_agua'], (i*bg_width_agua + self.state['scroll'], 414))
        self.state['scroll'] -= 1
        if abs(self.state['scroll']) > bg_width_agua:
            self.state['scroll'] = 0
        pygame.display.update()


class Personagem:
    def __init__(self, assets):
        pass

jogo = Jogo()
while jogo.eventos():
    jogo.desenha()
pygame.quit()