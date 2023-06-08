from .Semente import Semente

class Semente1(Semente):

    def __init__(self, nome, preco = 5, caminho_imagem = 'novo_prototipo/assets/ui/sprite_semente_TESTE.png', quantidade = 1):
        super().__init__(nome, preco, caminho_imagem, quantidade)
        self.__planta_a_ser_gerada = 'Planta 1'

    @property
    def planta_a_ser_gerada(self):
        return self.__planta_a_ser_gerada