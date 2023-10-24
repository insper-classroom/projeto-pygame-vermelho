import pygame
import math
from constantes import *

def inicializa():
    pygame.init()
    tela = pygame.display.set_mode((1200, 600), 0, 0)
    pygame.display.set_caption('Jogo')

    assets = {}
    assets['fundo'] = pygame.image.load('img/Backgroud.jpg')
    assets['fundo_agua'] = pygame.image.load('img/Background_agua.png')
    assets['sprite_idle'] = pygame.image.load('img/idle_personagem.jpg')
    assets['sprite_move'] = pygame.image.load('img/mov_personagem.jpg')
    assets['sprite_jump'] = pygame.image.load('img/jump_personagem.jpg')
    assets['sprite_dano'] = pygame.image.load('img/dano_personagem.jpg')
    assets['sprite_attack'] = pygame.image.load('img/attk1_personagem.jpg')
    assets['sprite_attack2'] = pygame.image.load('img/attk2_personagem.jpg')
    assets['sprite_morte'] = pygame.image.load('img/morte_personagem.jpg')
    assets['idle'] = load_spritesheet(assets['sprite_idle'], 1, 6)
    assets['move'] = load_spritesheet(assets['sprite_move'], 1, 7)
    assets['jump'] = load_spritesheet(assets['sprite_jump'], 1, 8)
    assets['dano'] = load_spritesheet(assets['sprite_dano'], 1, 2)
    assets['attack'] = load_spritesheet(assets['sprite_attack'], 1, 5)
    assets['attack2'] = load_spritesheet(assets['sprite_attack2'], 1, 5)
    assets['morte'] = load_spritesheet(assets['sprite_morte'], 1, 4)

    state = {}
    state['scroll'] = 0

    return tela , assets , state

def eventos():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False

    return True

def desenha(tela, assets, state):
    tela.fill(PRETO)
    bg_width = assets['fundo'].get_width()
    tiles = math.ceil(1200/bg_width) + 1
    for i in range(0, tiles):
        tela.blit(assets['fundo'], (i*bg_width + state['scroll'], 0))
    state['scroll'] -= 2
    if abs(state['scroll']) > bg_width:
        state['scroll'] = 0
    
    bg_width_agua = assets['fundo_agua'].get_width()
    tiles_agua = math.ceil(1200/bg_width_agua) + 1
    for i in range(0, tiles_agua):
        tela.blit(assets['fundo_agua'], (i*bg_width_agua + state['scroll'], 414))
    state['scroll'] -= 2
    if abs(state['scroll']) > bg_width_agua:
        state['scroll'] = 0
    pygame.display.update()



def load_spritesheet(spritesheet, rows, columns):
    # Calcula a largura e altura de cada sprite.
    sprite_width = spritesheet.get_width() // columns
    sprite_height = spritesheet.get_height() // rows
    
    # Percorre todos os sprites adicionando em uma lista.
    sprites = []
    for row in range(rows):
        for column in range(columns):
            # Calcula posição do sprite atual
            x = column * sprite_width
            y = row * sprite_height
            # Define o retângulo que contém o sprite atual
            dest_rect = pygame.Rect(x, y, sprite_width, sprite_height)

            # Cria uma imagem vazia do tamanho do sprite
            image = pygame.Surface((sprite_width, sprite_height), pygame.SRCALPHA)
            # Copia o sprite atual (do spritesheet) na imagem
            image.blit(spritesheet, (0, 0), dest_rect)
            sprites.append(image)
    return sprites


def game_loop():
    clock = pygame.time.Clock()
    tela, assets , state = inicializa()
    while eventos():
        clock.tick(60)
        desenha(tela, assets, state)
    pygame.quit()

game_loop()