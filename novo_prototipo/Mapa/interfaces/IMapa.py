from abc import ABC, abstractmethod
from pygame import Vector2
import pygame
from entidades.jogador.jogador import Jogador
from itens.sementes.ISemente import ISemente
from Mapa.Blocos.TerraArada import TerraArada

from menus.ClassesAbstratas.MenuGenerico import MenuGenerico

from Mapa.Camera import Camera
from Mapa.Climas.interfaces.IClima import IClima

class IMapa(ABC):

    @abstractmethod
    def __init__(self, observador, clima: IClima, tamanho=49):
        self.__entidades = []
        self.__grupoAll = Camera(tamanho)
        self.__grupoBlocos = pygame.sprite.Group()
        self.__grupoJogador = pygame.sprite.Group()
        self.__grupoEntidades = pygame.sprite.Group()
        self.__grupoPlantas = pygame.sprite.Group()
        self.__observadores = []
        self.__spawns = {}
        self.__clima = clima
        self.__id = None

        # Criar matriz dos blocos
        self.__blocos = [[ None for coluna in range(tamanho)]
                              for linha in range(tamanho)]
        
        self.adiciona_observador(observador)

        self.construir_blocos()
        self.adiciona_jogador()
    
    @abstractmethod
    def construir_blocos(self):
        pass

    @abstractmethod
    def tocar_musica(self):
        pass

    def notifica_atualiza_clima(self):
        self.__clima.notifica_atualiza_clima()
    
    def adiciona_observador(self, observador):
        self.__observadores.append(observador)

    def adiciona_jogador(self):
        self.__entidades.append(Jogador((self.__playerSpawnX, self.__playerSpawnY), [self.__grupoAll, self.__grupoJogador]))

    def adiciona_entidade(self, entidade):
        self.__grupoAll.add(entidade)

    def notifica_troca_mapa(self, mapa):
        self.__observadores[0].trocar_mapa_atual(mapa)

    def notifica_ativa_menu(self, menu: MenuGenerico):
        for observador in self.__observadores:
            observador.notifica_ativa_menu(menu)
    
    def troca_bloco(self, posicao_x_matriz, posicao_y_matriz, novo_bloco):
        self.__blocos[posicao_y_matriz][posicao_x_matriz] = novo_bloco
        return

    def plantar(self, posicao_x_matriz, posicao_y_matriz, semente: ISemente):
        posicao_planta = Vector2()
        posicao_planta.x = self.__blocos[posicao_y_matriz][posicao_x_matriz].rect.x + 32
        posicao_planta.y = self.__blocos[posicao_y_matriz][posicao_x_matriz].rect.y + 45
        planta = semente.constroi_planta(posicao_planta, [self.__grupoAll, self.__grupoPlantas])
        self.clima.adiciona_observador(planta)
        self.__blocos[posicao_y_matriz][posicao_x_matriz].adiciona_planta(planta)
        self.jogador.inventario.remover_item(semente)

    def exclui_entidade(self, entidade_a_ser_excluida):
        grupos_de_entidades = [self.__grupoAll, self.__grupoBlocos, self.__grupoJogador, self.__grupoEntidades, self.__grupoPlantas]
        for grupo in grupos_de_entidades:
            grupo.remove(entidade_a_ser_excluida)
    
    def notifica_exclui_barreira(self, mapa):
        self.controleMapa.desbloquear_mapa(mapa)

    def desenhar(self, tela: pygame.Surface):
        self.grupoAll.custom_draw(self.jogador)

    @property
    def observadores(self):
        return self.__observadores

    @property
    def plantas(self):
        return self.__grupoPlantas.sprites()
    
    @property
    def blocos(self):
        return self.__blocos
    
    @property
    def jogador(self):
        return self.__entidades[0]

    @property
    def entidades(self):
        return self.__entidades
    
    @property
    def grupoAll(self):
        return self.__grupoAll

    @property
    def grupoBlocos(self):
        return self.__grupoBlocos
    
    @property
    def grupoPlantas(self):
        return self.__grupoPlantas
    
    @grupoPlantas.setter
    def grupoPlantas(self, lista_de_plantas):
        self.__grupoPlantas = lista_de_plantas
    
    @property
    def grupoJogador(self):
        return self.__grupoJogador
    
    @property
    def grupoEntidades(self):
        return self.__grupoEntidades
    
    @property
    def observador(self):
        return self.__observador
    
    @property
    def spawns(self):
        return self.__spawns

    @property
    def controleMapa(self):
        return self.__observadores[0]

    @property
    def grupos(self):
        return [self.__grupoAll, self.__grupoBlocos, self.__grupoJogador, self.__grupoEntidades, self.__grupoPlantas]
    
    @property
    def clima(self):
        return self.__clima
    
    @clima.setter
    def clima(self, clima):
        self.__clima = clima
        return
    
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id):
        self.__id = id