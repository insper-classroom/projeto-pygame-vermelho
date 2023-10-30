import pygame
from classe_jogador import *
from pytmx.util_pygame import load_pygame

class TiledMap(pygame.sprite.Sprite):
    def __init__(self, pos, groups):  
        super().__init__(groups)
        self.tmx_data = None
        self.pos = pos

    '''
    Carrega o arquivo tmx e desenha os tiles na tela    
    '''
    def carregar_mapa(self, arquivo): # carrega o arquivo tmx
        self.tmx_data = load_pygame(arquivo)

    def desenhar_mapa(self, tela): # desenha os tiles na tela
        tiles = [] # lista de tiles
        for layer in self.tmx_data.visible_layers:
            if hasattr(layer, 'tiles'):
                for x, y, surf in layer.tiles():
                    pos = (x * 16, y * 16) # Ajusta a posição do tile
                    surf = pygame.transform.scale(surf, (16, 16))
                    tela.blit(surf, pos)
                    #adicionar o tile a lista de tiles
                    tiles.append(pygame.Rect(pos[0], pos[1], 16, 16))
        return tiles