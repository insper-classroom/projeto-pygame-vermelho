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
        self.relogio = pygame.time.Clock()

    def eventos(self):
        mapa = Mapa()
        jogador = Jogador(100, 100)
        while self.game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        jogador.set_velocidade_x(-1)
                    elif event.key == pygame.K_RIGHT:
                        jogador.set_velocidade_x(1)
                    elif event.key == pygame.K_UP:
                        jogador.set_velocidade_y(-3)
                    elif event.key == pygame.K_DOWN:
                        jogador.set_velocidade_y(3)
                if event.type == pygame.KEYUP:
                    jogador.set_velocidade_x(0)
                    jogador.set_velocidade_y(0)

                   
            jogador.mover()
            jogador.atualizar_animacao()
            mapa.desenha(self.tela)
            jogador.desenha(self.tela)
            self.relogio.tick(60)
            pygame.display.update()
        return True
jogo = Jogo()
jogo.eventos()
pygame.quit()       