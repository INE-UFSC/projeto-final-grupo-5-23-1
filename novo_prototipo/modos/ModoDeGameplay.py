from Mapa.Mapa import Mapa
from comandos.ComandoDeInteracao import ComandoDeInteracao
from .ClassesAbstratas.ModoComInventarioGenerico import ModoComInventarioGenerico
from Mapa.ControleMapa import ControleMapa

from estado import EstadoJogo
from comandos import ComandoMover

import pygame
from pygame.math import Vector2
'''
Esta classe implementa o modo de jogo Jogar, o qual tem os métodos
"checa_eventos", "update", "render";
'''
class ModoDeGameplay(ModoComInventarioGenerico):

    #[TODO] - Implentar a criacao do evento de interacao

    def __init__(self):
        super().__init__()
        # Game state
        self.__estado_jogo = EstadoJogo()
        
        # Rendering properties
        self.__tamanho_bloco = Vector2(64,64)        
        
        self.__controleMapa = ControleMapa(self)
        # All layers listen to game state events
        self.__estado_jogo.adiciona_observador(self.__controleMapa)

        # Controls
        self.__jogador = self.__controleMapa.mapa_atual.jogador
        self.__comandos = [ ]
        
    @property
    def comprimento_bloco(self):
        return int(self.__tamanho_bloco.x)

    @property
    def altura_bloco(self):
        return int(self.__tamanho_bloco.y)
    
    @property
    def jogador(self):
        return self.__jogador
    
    def set_jogador(self, jogador):
        self.__jogador = jogador

    def checa_eventos(self, delta_tempo):
        # Eventos Pygame
        direcao = Vector2()
        mouseClicked = False
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.notifyQuitRequested()
                break

            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_ESCAPE:
                    self.notifyShowMenuRequested()
                    break
                if event.key == pygame.K_e:
                    self.__comandos.append(ComandoDeInteracao(self.__jogador.posicao_matriz, self.__jogador.status, self.__controleMapa.mapa_atual.blocos, self.__jogador.item_atual))
                if event.key == pygame.K_i:
                    self.notifyShowInventoryRequested(self.__jogador.inventario, self.__jogador)

                if event.key == pygame.K_p:
                    self.__controleMapa.trocar_mapa_atual('savana')
                
                if event.key == pygame.K_o:
                    self.__controleMapa.trocar_mapa_atual('floresta')

                if event.key == pygame.K_l:
                    print(self.__controleMapa.mapa_atual.jogador.posicao)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouseClicked = True
        
        keys = pygame.key.get_pressed()

        # Direções ---
        if keys[pygame.K_w]:
            direcao.y = -1
            status = 'cima'
        elif keys[pygame.K_s]:
            direcao.y = 1
            status = 'baixo'
        else:
            direcao.y = 0

        if keys[pygame.K_d]:
            direcao.x = 1
            status = 'direita'
        elif keys[pygame.K_a]:
            direcao.x = -1
            status = 'esquerda'
        else:
            direcao.x = 0
        # -----------

                    
        # Keyboard controls the moves of the player's unit
        if direcao.x != 0 or direcao.y != 0:
            self.__comandos.append(
                ComandoMover(self.__controleMapa.mapa_atual.grupoBlocos,self.__jogador, direcao, status, delta_tempo)
            )

    def update(self):
        for comando in self.__comandos:
            comando.run()
        self.__comandos.clear()
        self.__estado_jogo.epoch += 1
        for planta in self.__controleMapa.mapa_atual.plantas:
            planta.update()
        self.__jogador.update()

        
    def render(self, tela):
        self.__controleMapa.mapa_atual.desenhar(tela)
