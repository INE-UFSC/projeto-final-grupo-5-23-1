from Mapa.Blocos.Bloco import Bloco
from abc import abstractmethod

class BlocoComInteracao(Bloco):

    def __init__(self, x, y, largura, altura, observador):
        super().__init__(x, y, largura, altura, observador)

    def notifica_troca_bloco(self, posicao_x_matriz, posicao_y_matriz, novo_bloco):
        self.observador.troca_bloco(posicao_x_matriz, posicao_y_matriz, novo_bloco)
    
    @abstractmethod
    def interagir(self, item):
        pass