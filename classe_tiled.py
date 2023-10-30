import pygame
from classe_jogador import *
from pytmx.util_pygame import load_pygame

class TiledMap(pygame.sprite.Sprite):
    def __init__(self, pos, groups):  
        super().__init__(groups)
        self.tmx_data = None
        self.pos = pos

    def carregar_mapa(self, arquivo):
        self.tmx_data = load_pygame(arquivo)

    def desenhar_mapa(self, tela):
        tiles = []
        for layer in self.tmx_data.visible_layers:
            if hasattr(layer, 'tiles'):
                for x, y, surf in layer.tiles():
                    pos = (x * 16, y * 16)
                    surf = pygame.transform.scale(surf, (16, 16))
                    tela.blit(surf, pos)
                    pygame.draw.rect(tela, (255, 255, 255), (pos[0], pos[1], 16, 16), 1)
                    #adicionar o tile a lista de tiles
                    tiles.append(pygame.Rect(pos[0], pos[1], 16, 16))
        return tiles