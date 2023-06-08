from comandos.Comando import Comando


class ComandoVenderItem(Comando):

    def __init__(self, item, jogador):
        self.__item = item
        self.__jogador = jogador
    
    def run(self):
        self.__jogador.adiciona_moedas(self.__item.preco)
        self.__jogador.inventario.remover_item(self.__item)