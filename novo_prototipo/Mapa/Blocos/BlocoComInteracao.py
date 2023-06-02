from Mapa.Blocos.Bloco import Bloco
from abc import abstractmethod

class BlocoComInteracao(Bloco):

    def __init__(self, pos, surf, groups, observador, colisao=False):
        super().__init__(pos, surf, groups, observador, colisao)

    def notifica_troca_bloco(self, posicao_x_matriz, posicao_y_matriz, novo_bloco):
        self.observador.troca_bloco(posicao_x_matriz, posicao_y_matriz, novo_bloco)
    
    @abstractmethod
    def interagir(self, item):
        pass