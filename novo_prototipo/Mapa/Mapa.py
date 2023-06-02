from pygame import Surface, Vector2
import pygame
from Mapa.Blocos.Grama import BlocoDeGrama
from Mapa.Blocos.agua import Agua
from Mapa.Blocos.Parede import Parede
from Mapa.interfaces.IMapa import IMapa
from entidades.jogador.jogador import Jogador
from entidades.vendedor import Vendedor
from plantas.Planta import Planta
from pytmx.util_pygame import load_pygame

class Mapa:
    def __init__(self):
        self.__id = 'floresta'
        self.__blocos = []
        self.__entidades = []
        self.__grupoBlocos = pygame.sprite.Group()
        self.__grupoJogador = pygame.sprite.Group()
        self.__grupoEntidades = pygame.sprite.Group()
        self.__grupoPlantas = pygame.sprite.Group()
        self.construir_blocos()
        self.adiciona_entidades()

    @property
    def plantas(self):
        return self.__grupoPlantas.sprites()
    
    @property
    def blocos(self):
        return self.__blocos
    
    @blocos.setter
    def blocos(self, blocos):
        self.__blocos = blocos
        return
    
    @property
    def id(self):
        return self.__id
    
    @property
    def jogador(self):
        return self.__entidades[0]

    @property
    def grupoBlocos(self):
        return self.__grupoBlocos
    
    def troca_bloco(self, posicao_x_matriz, posicao_y_matriz, novo_bloco):
        self.__blocos[posicao_y_matriz][posicao_x_matriz] = novo_bloco
        return
    
    def plantar(self, posicao_x_matriz, posicao_y_matriz, item):
        posicao_planta = Vector2()
        posicao_planta.x = self.__blocos[posicao_y_matriz][posicao_x_matriz].x + 32
        posicao_planta.y = self.__blocos[posicao_y_matriz][posicao_x_matriz].y + 40
        planta = Planta(item.planta_a_ser_gerada, posicao_planta, self.__grupoPlantas)
        self.__blocos[posicao_y_matriz][posicao_x_matriz].adiciona_planta(planta)
        self.jogador.inventario.remover_item(item)

    def construir_blocos(self):
        tmx_data = load_pygame('novo_prototipo/Mapa/Mapas/floresta.tmx')
        
        for layer in tmx_data.layers:
            if layer.name  == 'Fundo':
                for x, y, surf in layer.tiles():
                    pos = (x*64-1000, y*64-300)
                    Agua(pos= pos, surf= surf, groups=self.__grupoBlocos, observador=self)

            if layer.name == 'Parede':
                for x, y, surf in layer.tiles():
                    pos = (x*64-1000, y*64-300)
                    Parede(pos, surf, self.__grupoBlocos, self)

            if layer.name == 'Grama':
                for x, y, surf in layer.tiles():
                    pos = (x*64-1000, y*64-300)
                    BlocoDeGrama(pos, surf, self.__grupoBlocos, self)


    def adiciona_entidades(self):
        self.__entidades.append(Jogador((640,360), self.__grupoJogador))

    def desenhar(self, tela: Surface):
        for linha in (self.blocos):
            for bloco in linha:
                bloco.desenhar(tela)
        self.__grupoBlocos.draw(tela)
        self.__grupoPlantas.draw(tela)
        self.__grupoJogador.draw(tela)
