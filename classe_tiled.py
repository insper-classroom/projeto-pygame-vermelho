import pygame
from pytmx.util_pygame import load_pygame

class TiledMap(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.tmx_data = None
        self.pos = pos

    def carregar_mapa(self, arquivo):
        self.tmx_data = load_pygame(arquivo)

    def desenhar_mapa(self, tela):
        for layer in self.tmx_data.visible_layers:
            if hasattr(layer, 'tiles'):
                for x, y, surf in layer.tiles():
                    pos = (x * 16, y * 16)
                    tela.blit(surf, pos)
