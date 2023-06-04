from itens.Item import Item
from itens.ItemQuantizavel import ItemQuantizavel


class Inventario:
    def __init__(self, capacidade):
        self.__capacidade = capacidade
        self.__itens = []

    @property
    def itens(self):
        return self.__itens

    def adicionar_item(self, item_a_ser_adicionado):
        if isinstance(item_a_ser_adicionado, Item):
            if isinstance(item_a_ser_adicionado, ItemQuantizavel):
                lista_de_nomes = []
                for item in self.__itens:
                    lista_de_nomes.append(item.nome)

                if item_a_ser_adicionado.nome in lista_de_nomes:
                    indice_item = lista_de_nomes.index(item_a_ser_adicionado.nome)
                    self.__itens[indice_item].aumenta_quantidade(item_a_ser_adicionado.quantidade)
                elif len(self.__itens) < self.__capacidade:
                    self.__itens.append(item_a_ser_adicionado)
            elif len(self.__itens) < self.__capacidade:
                self.__itens.append(item_a_ser_adicionado)
                
    def remover_item(self, item):
        if item in self.__itens:  
            if isinstance(item, ItemQuantizavel):
                item.reduz_quantidade(1)
                if item.quantidade == 0:
                    self.__itens.remove(item)
                return
            if isinstance(item, Item):             
                    self.__itens.remove(item)
                    return
