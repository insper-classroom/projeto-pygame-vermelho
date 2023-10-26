import pygame
from constantes import *
from classe_jogador import *
from classe_mapa import *
from classe_tiled import *

class Jogo:
    def __init__(self):
        pygame.init()
        self.game = True
        self.tela = pygame.display.set_mode((1200, 600), 0, 0)
        pygame.display.set_caption('Jogo')
        self.relogio = pygame.time.Clock()

    def eventos(self):
        mapa = Mapa()
        jogador = Jogador(50, 50)
        mapatiled = TiledMap((0, 0), pygame.sprite.Group())
        mapatiled.carregar_mapa('Tiled\mapa.tmx')

        while self.game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        jogador.jump()
                    if event.key == pygame.K_RIGHT:
                        jogador.velocidade_x = 5
                    if event.key == pygame.K_LEFT:
                        jogador.velocidade_x = - 5
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        jogador.velocidade_x -= 5
                    if event.key == pygame.K_LEFT:
                        jogador.velocidade_x += 5


            jogador.update()
            mapa.desenha(self.tela)
            jogador.desenha(self.tela)
            mapatiled.desenhar_mapa(self.tela)
            self.relogio.tick(60)
            pygame.display.update()
        return True
    
jogo = Jogo()
jogo.eventos()
pygame.quit()