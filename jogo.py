import pygame
from constantes import *

def inicializa():
    pygame.init()
    tela = pygame.display.set_mode((800, 600), 0, 0)
    pygame.display.set_caption('Jogo')

    assets = {}
    return tela

def eventos():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False

    return True

def atualiza(tela):
    tela.fill((0, 0, 0))
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
    tela = inicializa()

    while eventos():
        atualiza(tela)

    pygame.quit()

game_loop()