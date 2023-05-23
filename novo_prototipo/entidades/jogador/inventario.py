from itens.Item import Item
from itens.ItemQuantizavel import ItemQuantizavel


class Inventario:
    def __init__(self, capacidade):
        self.__capacidade = capacidade
        self.__itens = []

    @property
    def itens(self):
        return self.__itens

    def adicionar_item(self, item):
        if isinstance(item, Item):
            if len(self.__itens) < self.__capacidade:
                self.__itens.append(item)
                
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
