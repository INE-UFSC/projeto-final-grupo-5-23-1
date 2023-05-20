from pygame import Surface
from abc import ABC, abstractmethod


class Bloco(ABC):
    def __init__(self, x, y, largura, altura, observador):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.__observador = observador

    @property
    def observador(self):
        return self.__observador
    
    @property
    def posicao_matriz(self):
        posicao_matriz = [self.x, self.y]
        for index, posicao in enumerate(posicao_matriz):
                posicao_matriz[index] = int((posicao // 64))
        return posicao_matriz

    @abstractmethod
    def desenhar(self, tela: Surface):
        pass