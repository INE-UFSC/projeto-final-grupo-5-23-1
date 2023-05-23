from itens.Item import Item


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
        if isinstance(item, Item):
            if item in self.__itens:
                self.__itens.remove(item)
