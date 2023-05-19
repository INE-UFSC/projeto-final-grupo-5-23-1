from .Command import Comando
from novo_prototipo.Mapa.Bloco import Bloco


class InteractCommand(Comando):
    """
    Esse comando interage com um bloco
    """
    def __init__(self, posicao, status, mapa, item):
        self.__posicao = posicao
        self.__status = status
        self.__mapa = mapa
        self.__item = item

    def encontra_bloco(self):
        posicao_x = self.__posicao.x
        posicao_y = self.__posicao.y

        if self.__status == 'direita':
            return self.__mapa[(posicao_x + 1)][posicao_y]
        elif self.__status == 'esquerda':
            return self.__mapa[(posicao_x - 1)][posicao_y]
        elif self.__status == 'cima':
            return self.__mapa[(posicao_x)][posicao_y - 1]
        elif self.__status == 'baixo':
            return self.__mapa[posicao_x][posicao_y + 1]

    def run(self):
        bloco = self.encontra_bloco()
        if isinstance(bloco, BlocoComInteracao):
            bloco.interagir()
