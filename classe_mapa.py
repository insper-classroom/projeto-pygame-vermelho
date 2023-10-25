import pygame
import math
from constantes import *

class Mapa:
    def __init__(self):
        self.assets = {}
        self.assets['fundo'] = pygame.image.load('img/Backgroud.jpg')
        self.assets['fundo_agua'] = pygame.image.load('img/Background_agua.png')
        self.state = {}
        self.state['scroll'] = 0
    
    def desenha(self, tela):
        bg_width = self.assets['fundo'].get_width()
        tiles = math.ceil(1200/bg_width) + 1
        for i in range(0, tiles):
            tela.blit(self.assets['fundo'], (i*bg_width + self.state['scroll'], 0))
        self.state['scroll'] -= 1
        if abs(self.state['scroll']) > bg_width:
            self.state['scroll'] = 0
        
        bg_width_agua = self.assets['fundo_agua'].get_width()
        tiles_agua = math.ceil(1200/bg_width_agua) + 1
        for i in range(0, tiles_agua):
            tela.blit(self.assets['fundo_agua'], (i*bg_width_agua + self.state['scroll'], 414))
        self.state['scroll'] -= 1
        if abs(self.state['scroll']) > bg_width_agua:
            self.state['scroll'] = 0