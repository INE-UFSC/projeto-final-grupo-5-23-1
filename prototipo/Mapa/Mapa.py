from pygame import Surface
from Mapa.Bloco import Bloco
from Interfaces.IMapa import IMapa

class Mapa(IMapa):
    def __init__(self):
        self.__id = 'campo'
        self.__blocos = []
        self.construir_blocos()

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

    def construir_blocos(self):
        largura_bloco = 60
        altura_bloco = 60
        qtd_blocos_x = 1280 // largura_bloco
        qtd_blocos_y = 720 // altura_bloco
        
        for x in range(qtd_blocos_x):
            for y in range(qtd_blocos_y):
                bloco = Bloco(x * largura_bloco, y * altura_bloco, largura_bloco, altura_bloco)
                self.blocos.append(bloco)

    def desenhar(self, tela: Surface):
        for bloco in self.blocos:
            bloco.desenhar(tela)