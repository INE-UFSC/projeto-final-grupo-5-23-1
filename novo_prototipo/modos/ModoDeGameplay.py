from Mapa.Mapa import Mapa
from comandos.ComandoDeInteracao import ComandoDeInteracao
from modos.MenuInventario import MenuInventario
from comandos.ComandoAbrirMenu import ComandoAbrirMenu
from .ClassesAbstratas.ModoGenerico import ModoGenerico

from estado import EstadoJogo
from comandos import ComandoMover

import pygame
from pygame.math import Vector2
'''
Esta classe implementa o modo de jogo Jogar, o qual tem os métodos
"checa_eventos", "update", "render";
'''
class ModoDeGameplay(ModoGenerico):

    def __init__(self):
        super().__init__()
        # Game state
        self.__estado_jogo = EstadoJogo()
        
        # Rendering properties
        self.__tamanho_bloco = Vector2(64,64)        
        
        self.__mapa = Mapa()
        # All layers listen to game state events
        self.__estado_jogo.adiciona_observador(self.__mapa)

        self.__jogador = self.__mapa.jogador
        self.__comandos = [ ]
        
    @property
    def comprimento_bloco(self):
        return int(self.__tamanho_bloco.x)

    @property
    def altura_bloco(self):
        return int(self.__tamanho_bloco.y)
    
    def desativa_menu(self):
        self.__estado_jogo.menu_ingame_ativo = False
        self.__estado_jogo.menu_ingame = None
    
    def __roda_comandos(self):
        for comando in self.__comandos:
            comando.run()
        self.__comandos.clear()
        if self.__estado_jogo.menu_ingame_ativo:
            self.__estado_jogo.menu_ingame.update()
        return
    
    def __atualiza_entidades(self):
        for planta in self.__mapa.plantas:
            planta.update()
        self.__jogador.update()
        return

    def checa_eventos(self, delta_tempo):
        # Eventos Pygame
        direcao = Vector2()
        mouseClicked = False
        eventos = pygame.event.get()
        for event in eventos:

            if event.type == pygame.QUIT:
                self.notifyQuitRequested()
                break
            if not self.__estado_jogo.menu_ingame_ativo:
                if event.type == pygame.KEYDOWN:
                    
                    if event.key == pygame.K_ESCAPE:
                        self.notifyShowMenuRequested()
                        break
                    if event.key == pygame.K_e:
                        self.__comandos.append(ComandoDeInteracao(self.__jogador.posicao_matriz, self.__jogador.status, self.__mapa.blocos, self.__jogador.item_atual))
                    if event.key == pygame.K_i:                  
                        self.__comandos.append(ComandoAbrirMenu(self.__estado_jogo, MenuInventario(self.__jogador.inventario, self.__jogador), self))
                        
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouseClicked = True
        
        if not self.__estado_jogo.menu_ingame_ativo:
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
                    ComandoMover(self.__mapa.blocos,self.__jogador, direcao, status, delta_tempo)
                )
        else:
            self.__estado_jogo.menu_ingame.checa_eventos(eventos)

    def update(self):
        self.__roda_comandos()
        self.__atualiza_entidades()
        self.__estado_jogo.epoch += 1
        
    def render(self, tela):
        self.__mapa.desenhar(tela)
        if self.__estado_jogo.menu_ingame_ativo:
            self.__estado_jogo.menu_ingame.render(tela)
