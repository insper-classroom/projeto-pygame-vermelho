# import pygame, sys
# from pytmx.util_pygame import load_pygame
# from constantes import *


# class TiledMap(pygame.sprite.Sprite):
#     def __init__(self, pos,surf, groups):
#         super().__init__(groups)
#         self.image = surf
#         self.rect = self.image.get_rect(topleft = pos)

# pygame.init()
# screen = pygame.display.set_mode((1280, 720))
# tmx_data = load_pygame('Tiled\mapa.tmx')
# sprite_group = pygame.sprite.Group()

# for layer in tmx_data.visible_layers:
#     if hasattr(layer, 'tiles'):
#         for x, y, surf in layer.tiles():
#             pos = (x*12, y*12)
#             TiledMap(pos=pos, surf=surf, groups=sprite_group)

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#     screen.fill((0,0,0))
#     sprite_group.draw(screen)
#     pygame.display.update()

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
                    pos = (x * 12, y * 12)
                    tela.blit(surf, pos)
