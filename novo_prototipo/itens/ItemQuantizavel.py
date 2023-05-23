from .Item import Item

class ItemQuantizavel(Item):

    def __init__(self, nome, quantidade):
        super().__init__(nome)
        self.__quantidade = quantidade

    def reduz_quantidade(self, quantidade_a_ser_reduzida):
        nova_quantidade = self.__quantidade - quantidade_a_ser_reduzida
        if nova_quantidade >= 0:
            self.__quantidade = nova_quantidade

    @property
    def quantidade(self):
        return self.__quantidade