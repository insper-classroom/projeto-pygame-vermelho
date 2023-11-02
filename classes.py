import pygame
from constantes import *
from classe_jogador import *
from classe_mapa import *
from classe_tiled import *
from classe_inimigo import *
from classe_telainicial import *
from classe_telagameover import *

class Jogo:
    def __init__(self):
        pygame.init()
        self.game = True
        self.tela = pygame.display.set_mode((1200, 600), 0, 0)
        pygame.display.set_caption('Urban Brawl')
        self.relogio = pygame.time.Clock()
        self.camera = pygame.Vector2(0, 0)

        #Músicas e sons
        pygame.mixer.music.load('Sons/Where Is My Mind 8 Bit.mp3')
        pygame.mixer.music.set_volume(0.2)
        self.comeco = pygame.mixer.Sound('Sons/game-start-6104.mp3')
        self.morte = pygame.mixer.Sound('Sons/game-over-arcade-6435.mp3')
        self.mortee = False

        '''
        Inicializa o grupo de inimigos
        '''
        self.grupo_inimigos = pygame.sprite.Group()
        inimigo1 = Inimigo(700, 367, 'inimigo1')
        inimigo2 = Inimigo(100, 543, 'inimigo2')
        inimigo3 = Inimigo(1100, 415, 'inimigo3')
        inimigo4 = Inimigo(1590, 447, 'inimigo4')
        self.grupo_inimigos.add(inimigo1)
        self.grupo_inimigos.add(inimigo2)
        self.grupo_inimigos.add(inimigo3)
        self.grupo_inimigos.add(inimigo4)
        self.inimigos_mortos = 0
        pygame.mixer.music.play()

    def eventos(self):
        tela = True
        mapa = Mapa() # Cria o fundo
        jogador = Jogador(8, 320, self.grupo_inimigos) # Cria o personagem
        mapatiled = TiledMap((0, 0), pygame.sprite.Group()) # Cria o mapa
        mapatiled.carregar_mapa('Tiled\mapa.tmx') # Carrega o mapa
        telagameover = Telagameover()

        '''
        Game Loop
        '''
        while self.game: # Loop principal
            if tela:
                telainicial = Telainicial()
                telainicial.desenha(self.tela)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.game = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.comeco.play()
                            tela = False
            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.game = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE or event.key == pygame.K_UP: # Pulo
                            jogador.jump()
                        if event.key == pygame.K_RIGHT or event.key == pygame.K_d: # Movimentação
                            jogador.moving_right = True
                            jogador.flip = False
                        if event.key == pygame.K_LEFT or event.key == pygame.K_a: # Movimentação
                            jogador.moving_left = True
                            jogador.flip = True

                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_RIGHT or event.key == pygame.K_d: # Movimentação
                            jogador.moving_right = False
                        if event.key == pygame.K_LEFT or event.key == pygame.K_a: # Movimentação
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
                    if inimigo.vida <= 0:
                        self.inimigos_mortos += 1
                        self.grupo_inimigos.remove(inimigo)
                    if self.inimigos_mortos == 4:
                        chefe = Inimigo(170, 670, 'chefe')
                        inimigo.chefe = True
                        self.inimigos_mortos = 0
                        self.grupo_inimigos.add(chefe)
                    if inimigo.vida > 0:
                        inimigo.desenha(self.tela, self.camera)
                        if ((inimigo.pos[0] - jogador.rect.x)**2 + (inimigo.pos[1] - jogador.rect.y)**2)**0.5 < 16:
                            if jogador.timer <= 0:
                                if jogador.velocidade_y > 0 and jogador.rect.bottom <= inimigo.rect.top:
                                    inimigo.vida -= 1
                                    jogador.velocidade_y = -10
                                else:
                                    jogador.vida -= 1
                                    jogador.timer = 180

                
                if jogador.timer > 0:
                    self.tela.blit(pygame.font.SysFont('arial', 30).render(f'Invencibilidade: {jogador.contador}', True, (255, 255, 255)), (0, 30))
                    jogador.timer -= 1
                    jogador.contador = jogador.timer // 60
                
                if jogador.vida <= 0:
                    if self.mortee == False:
                        self.morte.play()
                        self.mortee = True
                    telagameover.desenha(self.tela)
                
                self.relogio.tick(60)
                
            pygame.display.update()

        return True
    
jogo = Jogo()
jogo.eventos()
pygame.quit()