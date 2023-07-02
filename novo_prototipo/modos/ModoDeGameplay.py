from comandos import ComandoDeInteracao, ComandoAbrirMenu, ComandoMover
from comandos.ComandoDeslizar import ComandoDeslizar
from menus import MenuInventario, MenuGenerico
from estado.ClassesAbstratas.IEstadoJogo import IEstadoJogo
from menus.MenuHud import MenuHud
from .ClassesAbstratas.ModoGenerico import ModoGenerico
from Mapa.ControleMapa import ControleMapa
from Mapa.Blocos.Gelo import Gelo

import pygame
from pygame.math import Vector2
'''
Esta classe implementa o modo de jogo Jogar, o qual tem os métodos
"checa_eventos", "update", "render";
'''
class ModoDeGameplay(ModoGenerico):

    def __init__(self, estado_de_jogo: IEstadoJogo):
        super().__init__()
        # Game state
        self.__estado_jogo = estado_de_jogo
        
        # Rendering properties
        self.__tamanho_bloco = Vector2(64,64)        
        
        self.__controleMapa = ControleMapa(self)
        # All layers listen to game state events
        self.estado_jogo.adiciona_observador(self.__controleMapa)

        # Controls
        self.__jogador = self.__controleMapa.mapa_atual.jogador
        self.__comandos = [ ]

        # Menu do hud:
        self.__hud = MenuHud(self.__jogador.inventario, self.__jogador)
        
    @property
    def comprimento_bloco(self):
        return int(self.__tamanho_bloco.x)

    @property
    def altura_bloco(self):
        return int(self.__tamanho_bloco.y)
    
    @property
    def jogador(self):
        return self.__jogador
    
    @property
    def estado_jogo(self):
        return self.__estado_jogo
    
    def set_jogador(self, jogador):
        self.__jogador = jogador

    def desativa_menu(self):
        self.estado_jogo.desativa_menu()
        return
    
    def ativa_menu(self, menu: MenuGenerico, observador):
        self.estado_jogo.ativa_menu(menu, observador)
        return
    
    def __roda_comandos(self):
        for comando in self.__comandos:
            comando.run()
        self.__comandos.clear()
        if self.estado_jogo.menu_ingame_ativo:
            self.estado_jogo.menu_ingame.update()
        return
    
    def __atualiza_entidades(self):
        for mapa in self.__controleMapa.mapas.values():
            mapa.grupoPlantas.update()
            mapa.grupoBlocos.update()
            mapa.notifica_atualiza_clima()
        self.__jogador.update()
        return

    def checa_eventos(self, delta_tempo):
        # Eventos Pygame
        direcao = Vector2()
        eventos = pygame.event.get()
        
        for event in eventos:

            if event.type == pygame.QUIT:
                self.notifyQuitRequested()
                break

            if event.type == pygame.KEYDOWN:
                if not self.estado_jogo.menu_ingame_ativo:
                    if event.key == pygame.K_ESCAPE:
                        self.notifyShowMenuRequested()
                        break
                    if event.key == pygame.K_e or event.key == pygame.K_RETURN:
                        self.__comandos.append(ComandoDeInteracao(self.__jogador.posicao_matriz, self.__jogador.status, self.__controleMapa.mapa_atual.blocos, self.__jogador))
                    if event.key == pygame.K_i:
                        self.__comandos.append(ComandoAbrirMenu(MenuInventario(self.__jogador.inventario, self.__jogador), self))
                    # Remover:
                    if event.key == pygame.K_l:
                        print(self.__controleMapa.mapa_atual.jogador.posicao)
                    # --------

        if not self.estado_jogo.menu_ingame_ativo:
            keys = pygame.key.get_pressed()
            # Hud
            self.__hud.checa_eventos(eventos)
            # Direções ---
            if keys[pygame.K_w] or keys[pygame.K_UP]:
                direcao.y = -1
                status = 'cima'
            elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
                direcao.y = 1
                status = 'baixo'
            else:
                direcao.y = 0

            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                direcao.x = 1
                status = 'direita'
            elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
                direcao.x = -1
                status = 'esquerda'
            else:
                direcao.x = 0
            # -----------

            # Keybinds temporárias para teleportar entre mapas
            if keys[pygame.K_LCTRL] and keys[pygame.K_1]:
                self.__controleMapa.trocar_mapa_atual('Floresta')
            if keys[pygame.K_LCTRL] and keys[pygame.K_2]:
                self.__controleMapa.trocar_mapa_atual('Deserto')
            if keys[pygame.K_LCTRL] and keys[pygame.K_3]:
                self.__controleMapa.trocar_mapa_atual('Neve')
            if keys[pygame.K_LCTRL] and keys[pygame.K_4]:
                self.__controleMapa.trocar_mapa_atual('Planicie')
            if keys[pygame.K_LCTRL] and keys[pygame.K_5]:
                self.__controleMapa.trocar_mapa_atual('Caverna')
            if keys[pygame.K_LCTRL] and keys[pygame.K_6]:
                self.__controleMapa.trocar_mapa_atual('Transporte')
            if keys[pygame.K_LCTRL] and keys[pygame.K_9]:
                self.__jogador.set_moedas(self.__jogador.moedas + 100)

                        
            # Keyboard controls the moves of the player's unit
            posicao_jogador = self.__jogador.posicao_matriz
            onIce = isinstance(self.__controleMapa.mapa_atual.blocos[posicao_jogador[1]][posicao_jogador[0]], Gelo)
            if onIce:
                self.__comandos.append(
                    ComandoDeslizar(self.__jogador, self.jogador.status, delta_tempo)
                )
            elif direcao.x != 0 or direcao.y != 0:
                self.__comandos.append(
                    ComandoMover(self.__controleMapa.mapa_atual.grupoBlocos,self.__jogador, direcao, status, delta_tempo)
                )
        else:
            self.estado_jogo.menu_ingame.checa_eventos(eventos)

    def update(self):
        self.__roda_comandos()
        self.__hud.update(self.__jogador)
        self.__atualiza_entidades()
        self.estado_jogo.ticks += 1


    def render(self, tela):
        self.__controleMapa.mapa_atual.desenhar(tela)
        self.__hud.render(tela)
        if self.estado_jogo.menu_ingame_ativo:
            self.estado_jogo.menu_ingame.render(tela)
        