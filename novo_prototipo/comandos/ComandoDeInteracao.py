from .Comando import Comando
from Mapa.Blocos.interfaces.IBlocoComInteracao import IBlocoComInteracao


class ComandoDeInteracao(Comando):
    """
    Esse comando interage com um bloco
    """
    def __init__(self, posicao_matriz, status, matriz_blocos, jogador):
        self.__posicao_matriz = posicao_matriz
        self.__status = status
        self.__matriz_blocos = matriz_blocos
        self.__jogador = jogador

    def encontra_bloco(self):
        posicao_x = self.__posicao_matriz[0]
        posicao_y = self.__posicao_matriz[1]
        if self.__status == 'direita':
            return self.__matriz_blocos[posicao_y][(posicao_x + 1)]
        elif self.__status == 'esquerda':
            return self.__matriz_blocos[posicao_y][(posicao_x - 1)]
        elif self.__status == 'cima':
            return self.__matriz_blocos[posicao_y - 1][(posicao_x)]
        elif self.__status == 'baixo':
            return self.__matriz_blocos[posicao_y + 1][posicao_x]

    def run(self):
       # try:
        bloco = self.encontra_bloco()
        if isinstance(bloco, IBlocoComInteracao):
            bloco.interagir(self.__jogador)
        #except Exception as e:
         #   raise Exception(f"Falha na interação:\n {e}")

