from .Comando import Comando

class ComandoSelecionaItemAtual(Comando):

    def __init__(self, jogador, item):
        self.__jogador = jogador
        self.__item = item

    def run(self):
        self.__jogador.seleciona_item(self.__item)