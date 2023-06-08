from abc import ABC, abstractmethod
from pygame import Surface, Vector2
import pygame
from entidades.jogador.jogador import Jogador
from plantas.Planta import Planta

class IMapa(ABC):

    @abstractmethod
    def __init__(self, observador):
        self.__entidades = []
        self.__grupoAll = pygame.sprite.Group()
        self.__grupoBlocos = pygame.sprite.Group()
        self.__grupoJogador = pygame.sprite.Group()
        self.__grupoEntidades = pygame.sprite.Group()
        self.__grupoPlantas = pygame.sprite.Group()

        # Criar matriz dos blocos
        self.__blocos = [[ None for coluna in range(49)]
                              for linha in range(49)]
        
        self.__observador = observador

        self.construir_blocos()
        self.adiciona_entidades()

    @abstractmethod
    def construir_blocos(self):
        pass

    def adiciona_entidades(self):
        self.__entidades.append(Jogador((self.__playerSpawnX, self.__playerSpawnY), [self.__grupoAll, self.__grupoJogador]))

    def troca_bloco(self, posicao_x_matriz, posicao_y_matriz, novo_bloco):
        self.__blocos[posicao_y_matriz][posicao_x_matriz] = novo_bloco
        return
    
    def plantar(self, posicao_x_matriz, posicao_y_matriz, item):
        posicao_planta = Vector2()
        posicao_planta.x = self.__blocos[posicao_y_matriz][posicao_x_matriz].rect.x + 32
        posicao_planta.y = self.__blocos[posicao_y_matriz][posicao_x_matriz].rect.y + 40
        planta = Planta(item.planta_a_ser_gerada, posicao_planta, [self.__grupoAll, self.__grupoPlantas])
        self.__blocos[posicao_y_matriz][posicao_x_matriz].adiciona_planta(planta)
        self.jogador.inventario.remover_item(item)

    
    def desenhar(self, tela: pygame.Surface):
        self.__grupoBlocos.draw(tela)
        for linha in self.blocos:
            for bloco in linha:
                bloco.desenhar(tela)

        self.__grupoPlantas.draw(tela)
        self.__grupoEntidades.draw(tela)
        self.__grupoJogador.draw(tela)
    
    def set_jogador(self, jogador):
        for sprite in self.__grupoJogador.sprites():
            sprite.kill()
        self.__entidades[0] = jogador

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
    
    @property
    def grupoJogador(self):
        return self.__grupoJogador
    
    @property
    def grupoEntidades(self):
        return self.__grupoEntidades
    
    @property
    def observador(self):
        return self.__observador
    