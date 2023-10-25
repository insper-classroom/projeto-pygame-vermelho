import pygame
from constantes import *
from classe_jogador import *
from classe_mapa import *

class Jogo:
    def __init__(self):
        pygame.init()
        self.game = True
        self.tela = pygame.display.set_mode((1200, 600), 0, 0)
        pygame.display.set_caption('Jogo')

    def eventos(self):
        mapa = Mapa()
        jogador = Jogador(100, 100)
        while self.game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game = False
            mapa.desenha(self.tela)
            jogador.desenha(self.tela)
            pygame.display.update()
        return True
jogo = Jogo()
jogo.eventos()
pygame.quit()       