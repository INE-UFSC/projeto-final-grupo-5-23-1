from Mapa.Blocos.interfaces.IBloco import IBloco
from abc import abstractmethod

class IBlocoComInteracao(IBloco):

    def __init__(self, pos, surf, groups, observador, colisao=False):
        super().__init__(pos, surf, groups, observador, colisao)

    def notifica_troca_bloco(self, posicao_x_matriz, posicao_y_matriz, novo_bloco):
        self.observador.troca_bloco(posicao_x_matriz, posicao_y_matriz, novo_bloco)

    def notifica_adiciona_entidade(self, entidade):
        self.observador.adiciona_entidade(entidade)

    def notifica_exclui_entidade(self, entidade):
        self.observador.exclui_entidade(entidade)

    @abstractmethod
    def interagir(self, jogador):
        pass