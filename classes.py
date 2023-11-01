import pygame
from constantes import *
from classe_jogador import *
from classe_mapa import *
from classe_tiled import *
from classe_inimigo import *

class Jogo:
    def __init__(self):
        pygame.init()
        self.game = True
        self.tela = pygame.display.set_mode((1200, 600), 0, 0)
        pygame.display.set_caption('Urban Brawl')
        self.relogio = pygame.time.Clock()
        self.camera = pygame.Vector2(0, 0)
        self.grupo_inimigos = pygame.sprite.Group() # Cria o grupo de inimigos
        inimigo1 = Inimigo(700, 367, 'inimigo1') # Cria o inimigo
        inimigo2 = Inimigo(100, 543, 'inimigo2') # Cria o inimigo
        inimigo3 = Inimigo(1100, 415, 'inimigo3') # Cria o inimigo
        inimigo4 = Inimigo(1590, 447, 'inimigo4') # Cria o inimigo
        self.grupo_inimigos.add(inimigo1) # Adiciona o inimigo ao grupo
        self.grupo_inimigos.add(inimigo2)
        self.grupo_inimigos.add(inimigo3)
        self.grupo_inimigos.add(inimigo4)

    def eventos(self):
        mapa = Mapa() # Cria o fundo
        jogador = Jogador(8, 320, self.grupo_inimigos) # Cria o personagem
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
                    if event.key == pygame.K_UP: # Pulo
                        jogador.jump()
                    if event.key == pygame.K_RIGHT: # Movimentação
                        jogador.moving_right = True
                        jogador.flip = False
                    if event.key == pygame.K_LEFT: # Movimentação
                        jogador.moving_left = True
                        jogador.flip = True
                    if event.key == pygame.K_SPACE:
                        jogador.atacar()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT: # Movimentação
                        jogador.moving_right = False
                    if event.key == pygame.K_LEFT: # Movimentação
                        jogador.moving_left = False
                
            if jogador.rect.y > 600:
                self.game = False

            '''
            Atualizações
            '''
            self.camera.x = jogador.rect.x
            self.camera.y = 300
            self.grupo_inimigos.update()

            mapa.desenha(self.tela) # Desenha o fundo
            mapatiled.desenhar_mapa(self.tela, self.camera) # Desenha o mapaa
            jogador.desenha(self.tela) # Desenha o personagem
            jogador.update(mapatiled.desenhar_mapa(self.tela,self.camera)) # Atualiza a posição do personagem
            
            for inimigo in self.grupo_inimigos:
                inimigo.desenha(self.tela, self.camera)
                if ((inimigo.pos[0] - jogador.rect.x)**2 + (inimigo.pos[1] - jogador.rect.y)**2)**0.5 < 16:
                    if jogador.timer <= 0:
                        jogador.vida -= 1
                        jogador.timer = 180
            self.relogio.tick(60)

            if jogador.timer > 0:
                self.tela.blit(pygame.font.SysFont('arial', 30).render(f'Invencibilidade: {jogador.contador}', True, (255, 255, 255)), (0, 0))
                jogador.timer -= 1
                jogador.contador = jogador.timer // 60
            if jogador.vida <= 0:
                self.game = False
            
            pygame.display.update()

        return True
    
jogo = Jogo()
jogo.eventos()
pygame.quit()