from .Semente import Semente

class Semente1(Semente):

    def __init__(self, nome):
        super().__init__(nome)
        self.__planta_a_ser_gerada = 'Planta 1'

    @property
    def planta_a_ser_gerada(self):
        return self.__planta_a_ser_gerada