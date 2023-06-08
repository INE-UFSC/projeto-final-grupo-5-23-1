from comandos.Comando import Comando


class ComandoComprarItem(Comando):

    def __init__(self, item, jogador):
        self.__item = item
        self.__jogador = jogador
    
    def run(self):
        if self.__jogador.moedas - self.__item.preco >= 0:
            self.__jogador.remove_moedas(self.__item.preco)
            self.__jogador.inventario.adicionar_item(self.__item)