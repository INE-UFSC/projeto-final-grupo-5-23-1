from itens.Item import Item
from comandos.Comando import Comando
from itens.ItemQuantizavel import ItemQuantizavel


class ComandoComprarItem(Comando):

    def __init__(self, item, jogador):
        self.__item = item
        self.__jogador = jogador
    
    def run(self):
        lista_nomes_itens = []
        for item in self.__jogador.inventario.itens:
            if isinstance(item, Item):
                lista_nomes_itens.append(item.nome)
        if (self.__jogador.inventario.capacidade_atual < self.__jogador.inventario.capacidade_maxima) or (isinstance(self.__item, ItemQuantizavel) and self.__item.nome in  lista_nomes_itens):
            if self.__jogador.moedas - self.__item.preco >= 0:
                self.__jogador.remove_moedas(self.__item.preco)
                self.__jogador.inventario.adicionar_item(self.__item)