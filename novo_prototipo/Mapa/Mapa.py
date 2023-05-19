from pygame import Surface
import pygame
from Mapa.Bloco import Bloco
from Mapa.interfaces.IMapa import IMapa
from entidades.jogador.jogador import Jogador

class Mapa(IMapa):
    def __init__(self):
        self.__id = 'campo'
        self.__blocos = []
        self.__entidades = []
        self.__grupoJogador = pygame.sprite.Group()
        self.construir_blocos()
        self.adiciona_entidades()

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

    def construir_blocos(self):
        largura_bloco = 64
        altura_bloco = 64
        qtd_blocos_x = 768 // largura_bloco
        qtd_blocos_y = 1280 // altura_bloco
        
        for x in range(qtd_blocos_x):
            linha = []
            for y in range(qtd_blocos_y):
                bloco = Bloco(x * largura_bloco, y * altura_bloco, largura_bloco, altura_bloco)
                self.blocos.append(bloco)

    def adiciona_entidades(self):
        self.__entidades.append(Jogador((640,360), self.__grupoJogador))

    def desenhar(self, tela: Surface):
        for linha in (self.blocos):
            for bloco in linha:
                bloco.desenhar(tela)
        self.__grupoJogador.draw(tela)

