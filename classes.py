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
        pygame.display.set_caption('Urban Brawl')
        self.relogio = pygame.time.Clock()

    def eventos(self):
        mapa = Mapa() # Cria o fundo
        jogador = Jogador(50, 50) # Cria o personagem
        mapatiled = TiledMap((0, 0), pygame.sprite.Group()) # Cria o mapa
        mapatiled.carregar_mapa('Tiled\mapa.tmx') # Carrega o mapa
        '''
        Game Loop
        '''
        while self.game: # Loop principal
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE: # Pulo
                        jogador.jump()
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d: # Movimentação
                        jogador.moving_right = True
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a: # Movimentação
                        jogador.moving_left = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d: # Movimentação
                        jogador.moving_right = False
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a: # Movimentação
                        jogador.moving_left = False


            '''
            Atualizações
            '''
            mapa.desenha(self.tela) # Desenha o fundo
            mapatiled.desenhar_mapa(self.tela) # Desenha o mapa
            jogador.desenha(self.tela) # Desenha o personagem
            jogador.update(mapatiled.desenhar_mapa(self.tela)) # Atualiza a posição do personagem
            self.relogio.tick(60)
            pygame.display.update()

        return True
    
jogo = Jogo()
jogo.eventos()
pygame.quit()