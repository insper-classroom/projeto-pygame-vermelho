import pygame
from constantes import *
from classe_jogador import *
from classe_mapa import *
from classe_tiled import *
from classe_inimigo import *
from classe_telainicial import *
from classe_telagameover import *
from classe_cura import *
from classe_telawin import *

class Jogo:
    def __init__(self):
        '''
        Inicializa o jogo
        '''
        pygame.init()
        pygame.joystick.init()
        self.joystick = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
        for joy in self.joystick:
            joy.init()
        
        self.game = True
        self.tela = pygame.display.set_mode((1200, 600), 0, 0)
        pygame.display.set_caption('Urban Brawl')
        self.boneco_morto = pygame.image.load('img/personagem-principal-morto.png')
        self.boneco_morto = pygame.transform.scale(self.boneco_morto, (300, 200))
        self.relogio = pygame.time.Clock()
        self.camera = pygame.Vector2(0, 0)
        self.t0 = 0

        #Músicas e sons
        pygame.mixer.music.load('Sons/Where Is My Mind 8 Bit.mp3')
        pygame.mixer.music.set_volume(0.5)
        self.comeco = pygame.mixer.Sound('Sons/game-start-6104.mp3')
        self.morte = pygame.mixer.Sound('Sons/game-over-arcade-6435.mp3')
        self.morte_inimigo = pygame.mixer.Sound('Sons/morte 8bit.mp3')
        self.morte_inimigo.set_volume(1.5)
        self.pulo = pygame.mixer.Sound('Sons/8bit-jump.mp3')
        self.pulo.set_volume(0.2)
        self.dano = pygame.mixer.Sound('Sons/minecraft-damage_OTtnom6.mp3')
        self.curar = pygame.mixer.Sound('Sons/heal.mp3')
        self.curar.set_volume(0.5)
        self.mortee = False

        '''
        Inicializa o grupo de inimigos
        '''
        self.grupo_inimigos = pygame.sprite.Group()
        inimigo1 = Inimigo(700, 367, 'inimigo1')
        inimigo2 = Inimigo(100, 543, 'inimigo2')
        inimigo3 = Inimigo(1100, 415, 'inimigo3')
        inimigo4 = Inimigo(1590, 447, 'inimigo4')
        inimigo5 = Inimigo(1550, 622, 'inimigo1')
        inimigo7 = Inimigo(1080, 590, 'inimigo2')
        inimigo6 = Inimigo(500, 670, 'inimigo3')
        self.grupo_inimigos.add(inimigo1)
        self.grupo_inimigos.add(inimigo2)
        self.grupo_inimigos.add(inimigo3)
        self.grupo_inimigos.add(inimigo4)
        self.grupo_inimigos.add(inimigo5)
        self.grupo_inimigos.add(inimigo6)
        self.grupo_inimigos.add(inimigo7)
        self.inimigos_mortos = 0

        self.grupo_inimigos_tutorial = pygame.sprite.Group()
        self.grupo_cura_tutorial = pygame.sprite.Group()
        inimigo_tutorial = Inimigo(1000, 607, 'inimigo2')
        cura_tutorial = Cura(800, 670)
        self.grupo_cura_tutorial.add(cura_tutorial)
        self.grupo_inimigos_tutorial.add(inimigo_tutorial)
        self.inimigos_mortos_tutorial = 0

        '''
        Inicializa o grupo de curas
        '''
        self.grupo_cura = pygame.sprite.Group()
        cura1 = Cura(1100, 370)
        cura2 = Cura(500, 443)
        cura3 = Cura(1400, 560)
        self.grupo_cura.add(cura1)
        self.grupo_cura.add(cura2)
        self.grupo_cura.add(cura3)
    
    def reiniciar(self):
        '''
        Reinicia o jogo
        '''
        self.game = True
        self.tela = pygame.display.set_mode((1200, 600), 0, 0)
        pygame.display.set_caption('Urban Brawl')
        self.boneco_morto = pygame.image.load('img/personagem-principal-morto.png')
        self.boneco_morto = pygame.transform.scale(self.boneco_morto, (300, 200))
        self.relogio = pygame.time.Clock()
        self.camera = pygame.Vector2(0, 0)
        self.t0 = 0

        #Músicas e sons
        pygame.mixer.music.load('Sons/Where Is My Mind 8 Bit.mp3')
        pygame.mixer.music.set_volume(0.5)
        self.comeco = pygame.mixer.Sound('Sons/game-start-6104.mp3')
        self.morte = pygame.mixer.Sound('Sons/game-over-arcade-6435.mp3')
        self.morte_inimigo = pygame.mixer.Sound('Sons/morte 8bit.mp3')
        self.morte_inimigo.set_volume(1.5)
        self.pulo = pygame.mixer.Sound('Sons/8bit-jump.mp3')
        self.pulo.set_volume(0.2)
        self.dano = pygame.mixer.Sound('Sons/minecraft-damage_OTtnom6.mp3')
        self.curar = pygame.mixer.Sound('Sons/heal.mp3')
        self.curar.set_volume(0.5)
        self.mortee = False

        '''
        Inicializa o grupo de inimigos
        '''
        self.grupo_inimigos = pygame.sprite.Group()
        inimigo1 = Inimigo(700, 367, 'inimigo1')
        inimigo2 = Inimigo(100, 543, 'inimigo2')
        inimigo3 = Inimigo(1100, 415, 'inimigo3')
        inimigo4 = Inimigo(1590, 447, 'inimigo4')
        inimigo5 = Inimigo(1550, 622, 'inimigo1')
        inimigo7 = Inimigo(1080, 590, 'inimigo2')
        inimigo6 = Inimigo(500, 670, 'inimigo3')
        self.grupo_inimigos.add(inimigo1)
        self.grupo_inimigos.add(inimigo2)
        self.grupo_inimigos.add(inimigo3)
        self.grupo_inimigos.add(inimigo4)
        self.grupo_inimigos.add(inimigo5)
        self.grupo_inimigos.add(inimigo6)
        self.grupo_inimigos.add(inimigo7)
        self.inimigos_mortos = 0

        self.grupo_inimigos_tutorial = pygame.sprite.Group()
        self.grupo_cura_tutorial = pygame.sprite.Group()
        inimigo_tutorial = Inimigo(1000, 607, 'inimigo2')
        cura_tutorial = Cura(800, 670)
        self.grupo_cura_tutorial.add(cura_tutorial)
        self.grupo_inimigos_tutorial.add(inimigo_tutorial)
        self.inimigos_mortos_tutorial = 0

        '''
        Inicializa o grupo de curas
        '''
        self.grupo_cura = pygame.sprite.Group()
        cura1 = Cura(1100, 370)
        cura2 = Cura(500, 443)
        cura3 = Cura(1400, 560)
        self.grupo_cura.add(cura1)
        self.grupo_cura.add(cura2)
        self.grupo_cura.add(cura3)

    def eventos(self):
        tutorial = False
        tela = True
        ganhar = False
        self.ja_passado = 0
        mapa = Mapa() # Cria o fundo
        jogador = Jogador(8, 320, self.grupo_inimigos) # Cria o personagem
        mapatiled = TiledMap((0, 0), pygame.sprite.Group()) # Cria o mapa
        mapatiled.carregar_mapa('Tiled\mapa.tmx') # Carrega o mapa
        telagameover = Telagameover()
        telawin = TelaWin()

        '''
        Game Loop
        '''
        while self.game: # Loop principal
            if tutorial: # Tela do tutorial
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.game = False
                    if event.type == pygame.JOYAXISMOTION:
                        if event.axis == 0:
                            if event.value > 0.5:
                                jogador.moving_right = True
                                jogador.flip = False
                            elif event.value < -0.5:
                                jogador.moving_left = True
                                jogador.flip = True
                            else:
                                jogador.moving_right = False
                                jogador.moving_left = False
                    if event.type == pygame.JOYBUTTONDOWN:
                        if event.button == 7:
                            tutorial = False
                            jogador.rect.x = 8
                            jogador.rect.y = 320
                            jogador.vida = 3
                            jogador.timer = 0
                            jogador.contador = 0
                            jogador.morto = False
                            self.t0 = pygame.time.get_ticks()
                            pygame.mixer.music.play()
                        
                        if event.button == 0:
                            jogador.jump()
                            self.pulo.play()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            tutorial = False
                            jogador.rect.x = 8
                            jogador.rect.y = 320
                            jogador.vida = 3
                            jogador.timer = 0
                            jogador.contador = 0
                            jogador.morto = False
                            self.t0 = pygame.time.get_ticks()
                            pygame.mixer.music.play()

                        if event.key == pygame.K_RIGHT or event.key == pygame.K_d: # Movimentação
                            jogador.moving_right = True
                            jogador.flip = False
                        if event.key == pygame.K_LEFT or event.key == pygame.K_a: # Movimentação
                            jogador.moving_left = True
                            jogador.flip = True
                        if event.key == pygame.K_SPACE or event.key == pygame.K_UP: # Pulo
                            jogador.jump()
                            self.pulo.play()

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

                mapatiled.desenhar_tutorial(self.tela, self.camera)
                self.tela.fill((0, 0, 0))
                self.tela.blit(pygame.font.SysFont('arial', 30).render('Para Prosseguir ao jogo elimine todos os inimigos', True, (255, 255, 255)), (0, 30))
                self.tela.blit(pygame.font.SysFont('arial', 30).render('Como jogar: controle para mover o personagem e apeete A para pular', True, (255, 255, 255)), (0, 60))
                self.tela.blit(pygame.font.SysFont('arial', 30).render('Cada sabão pego gannha 1 de vida (Maximo de 5)', True, (255, 255, 255)), (0, 90))
                self.tela.blit(pygame.font.SysFont('arial', 30).render('Para eliminar um inimigo pule na cabeça dele', True, (255, 255, 255)), (0, 120))
                jogador.desenha(self.tela)
                jogador.update(mapatiled.desenhar_tutorial(self.tela,self.camera))

                for cura in self.grupo_cura_tutorial:
                    cura.rotacao()
                    cura.desenha(self.tela, self.camera)
                    if ((cura.pos[0] - jogador.rect.x)**2 + (cura.pos[1] - jogador.rect.y)**2)**0.5 < 32 and jogador.vida < 5:
                        jogador.vida += 1
                        self.grupo_cura_tutorial.remove(cura)
                        self.curar.play()
                
                for inimigo in self.grupo_inimigos_tutorial:
                    if inimigo.vida <= 0:
                        self.inimigos_mortos_tutorial += 1
                        self.morte_inimigo.play()
                        self.grupo_inimigos_tutorial.remove(inimigo)
                    if inimigo.vida > 0:
                        inimigo.desenha(self.tela, self.camera)
                        if ((inimigo.pos[0] - jogador.rect.x)**2 + (inimigo.pos[1] - jogador.rect.y)**2)**0.5 < 16:
                            if jogador.timer <= 0:
                                if jogador.velocidade_y > 0 and jogador.rect.bottom <= inimigo.rect.top:
                                    inimigo.vida -= 1
                                    jogador.velocidade_y = -10
            
                if self.inimigos_mortos_tutorial == 1:
                    tutorial = False
                    jogador.rect.x = 8
                    jogador.rect.y = 320
                    jogador.vida = 3
                    jogador.timer = 0
                    jogador.contador = 0
                    jogador.morto = False
                    self.t0 = pygame.time.get_ticks()
                    pygame.mixer.music.play()

            elif tela:
                # Tela inicial
                telainicial = Telainicial()
                telainicial.desenha(self.tela)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.game = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.comeco.play()
                            tela = False
                            tutorial = True
                    if event.type == pygame.JOYBUTTONDOWN:
                        if event.button == 0:
                            self.comeco.play()
                            tela = False
                            tutorial = True
            
            else:
                # Tela do jogo principal
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.game = False
                    if event.type == pygame.JOYAXISMOTION:
                        if event.axis == 0:
                            if event.value > 0.5:
                                jogador.moving_right = True
                                jogador.flip = False
                            elif event.value < -0.5:
                                jogador.moving_left = True
                                jogador.flip = True
                            else:
                                jogador.moving_right = False
                                jogador.moving_left = False
                    if event.type == pygame.JOYBUTTONDOWN:
                        if event.button == 0:
                            jogador.jump()
                            self.pulo.play()
                        if jogador.morto and event.button == 0:
                            self.timer = 0
                            self.ja_passado = pygame.time.get_ticks()
                            jogador.rect.x = 8
                            jogador.rect.y = 320
                            jogador.vida = 3
                            jogador.morto = False
                            self.reiniciar()
                            pygame.mixer.music.play()

                    if event.type == pygame.KEYDOWN:
                        if jogador.morto and event.key == pygame.K_SPACE:
                            self.timer = 0
                            self.ja_passado = pygame.time.get_ticks()
                            jogador.rect.x = 8
                            jogador.rect.y = 320
                            jogador.vida = 3
                            jogador.morto = False
                            self.reiniciar()
                            pygame.mixer.music.play()
                        
                        if event.key == pygame.K_RIGHT or event.key == pygame.K_d: # Movimentação
                            jogador.moving_right = True
                            jogador.flip = False
                        if event.key == pygame.K_LEFT or event.key == pygame.K_a: # Movimentação
                            jogador.moving_left = True
                            jogador.flip = True
                        if event.key == pygame.K_SPACE or event.key == pygame.K_UP: # Pulo
                            jogador.jump()
                            self.pulo.play()

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

                if ganhar == False:
                    t1 = pygame.time.get_ticks()
                    self.timer = ((t1 - self.ja_passado) - self.t0) // 1000

                self.tela.fill((0, 0, 0))
                mapa.desenha(self.tela, self.camera ) # Desenha o fundo
                mapatiled.desenhar_mapa(self.tela, self.camera) # Desenha o mapaa
                jogador.desenha(self.tela) # Desenha o personagem
                jogador.update(mapatiled.desenhar_mapa(self.tela,self.camera)) # Atualiza a posição do personagem
                self.tela.blit(pygame.font.SysFont('arial', 30).render(f'Tempo: {self.timer}', True, (255, 255, 255)), (1000, 0))
                
                for cura in self.grupo_cura:
                    cura.rotacao()
                    cura.desenha(self.tela, self.camera)
                    if ((cura.pos[0] - jogador.rect.x)**2 + (cura.pos[1] - jogador.rect.y)**2)**0.5 < 32 and jogador.vida < 5:
                        jogador.vida += 1
                        self.grupo_cura.remove(cura)
                        self.curar.play()
                
                for inimigo in self.grupo_inimigos:
                    if inimigo.vida <= 0:
                        self.inimigos_mortos += 1
                        self.morte_inimigo.play()
                        self.grupo_inimigos.remove(inimigo)
                    if self.inimigos_mortos == 7:
                        chefe = Inimigo(170, 670, 'chefe')
                        inimigo.chefe = True
                        self.inimigos_mortos = 8
                        self.grupo_inimigos.add(chefe)

                    if inimigo.vida > 0:
                        inimigo.desenha(self.tela, self.camera)
                        if ((inimigo.pos[0] - jogador.rect.x)**2 + (inimigo.pos[1] - jogador.rect.y)**2)**0.5 < 16:
                            if jogador.timer <= 0:
                                if jogador.velocidade_y > 0 and jogador.rect.bottom <= inimigo.rect.top:
                                    inimigo.vida -= 1
                                    jogador.velocidade_y = -10
                                else:
                                    self.dano.play()
                                    jogador.vida -= 1
                                    jogador.timer = 180

                if self.inimigos_mortos == 9:
                    ganhar = True

                if jogador.timer > 0:
                    self.tela.blit(pygame.font.SysFont('arial', 30).render(f'Invencibilidade: {jogador.contador}', True, (255, 255, 255)), (0, 30))
                    jogador.timer -= 1
                    jogador.contador = jogador.timer // 60
                

                if jogador.vida <= 0:
                    if self.mortee == False:
                        pygame.mixer.music.stop()
                        self.morte.play()
                        self.mortee = True
                    telagameover.desenha(self.tela)
                    self.tela.blit(pygame.font.SysFont('arial', 30).render(f'Voce consegue, pressione A para recomecar a fase', True, (255, 255, 255)), (565, 560))
                    self.tela.blit(self.boneco_morto, (50,400))
                    jogador.morto = True
                
                if ganhar:
                    pygame.mixer.music.stop()
                    telawin.desenha(self.tela)
                    self.tela.blit(pygame.font.SysFont('arial', 30).render(f'Seu tempo foi de {self.timer}', True, (0, 0, 0)), (482, 375))
                
                self.relogio.tick(60)
                
            pygame.display.update()
            

        return True
    
jogo = Jogo()
jogo.eventos()
pygame.quit()