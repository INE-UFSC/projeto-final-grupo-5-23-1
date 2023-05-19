from modos import ObservadorModoDeJogo, ModoDeMenu, ModoDeGameplay, ModoDeMensagem

import os
import pygame

os.environ['SDL_VIDEO_CENTERED'] = '1'

class Sistema(ObservadorModoDeJogo):
    def __init__(self):
        # Janela
        pygame.init()
        self.window = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Vale dos cultivos")

        '''
        Coloca os atributos base para o ciclo do jogo
        '''
        # Modos de 'jogo'
        self.__modo_de_jogo = ModoDeGameplay()
        self.__modo_de_jogo.adiciona_observador(self)
        self.__modo_de_overlay = ModoDeMenu()
        self.__modo_de_overlay.adiciona_observador(self)
        self.__modo_ativo = 'Jogo'
        
        # Propriedades do pygame
        self.__clock = pygame.time.Clock()
        self.__fps = 60
        self.__rodando = True        

    def mostra_mensagem(self, message):
        self.overlayGameMode = ModoDeMensagem(message)
        self.overlayGameMode.adiciona_observador(self)
        self.currentActiveMode = 'Overlay'

    def worldSizeChanged(self, worldSize):
        self.window = pygame.display.set_mode((int(worldSize.x),int(worldSize.y)))
        
    def showGameRequested(self):
        if self.__modo_de_jogo is not None:
            self.__modo_ativo = 'Jogo'

    def showMenuRequested(self):
        self.__modo_de_overlay = ModoDeMenu()
        self.__modo_de_overlay.adiciona_observador(self)
        self.__modo_ativo = 'Overlay'
        
    def quitRequested(self):
        self.__rodando = False
       
    def run(self):
        while self.__rodando:
            # Os eventos e updates são exclusivos dos modos
            if self.__modo_ativo == 'Overlay':
                self.__modo_de_overlay.checa_eventos()
                self.__modo_de_overlay.update()
            elif self.__modo_de_jogo is not None:
                delta_tempo = self.__clock.tick(self.__fps) / 200
                self.__modo_de_jogo.checa_eventos(delta_tempo)
                try:
                    self.__modo_de_jogo.update()
                except Exception as ex:
                    print(ex)
                    self.__modo_de_jogo = None
                    self.mostra_mensagem("Erro durante o update...")
                    
            # Renderiza o jogo (se ter algum), e então o overlay (se estiver ativo)
            if self.__modo_de_jogo is not None:
                self.__modo_de_jogo.render(self.window)
            else:
                self.window.fill((0,0,0))
            if self.__modo_ativo == 'Overlay':
                darkSurface = pygame.Surface(self.window.get_size(),flags=pygame.SRCALPHA)
                pygame.draw.rect(darkSurface, (0,0,0,150), darkSurface.get_rect())
                self.window.blit(darkSurface, (0,0))
                self.__modo_de_overlay.render(self.window)
                
            # Update display
            pygame.display.update()    
            self.__clock.tick(self.__fps)
            
     
Sistema = Sistema()
Sistema.run()
           
pygame.quit()