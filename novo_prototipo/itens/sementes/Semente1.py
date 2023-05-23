from .Semente import Semente

class Semente1(Semente):

    def __init__(self, nome, quantidade):
        super().__init__(nome, quantidade)
        self.__planta_a_ser_gerada = 'Planta 1'

    @property
    def planta_a_ser_gerada(self):
        return self.__planta_a_ser_gerada