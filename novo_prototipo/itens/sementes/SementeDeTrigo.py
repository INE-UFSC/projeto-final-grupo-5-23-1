from plantas.interfaces.IPlanta import IPlanta
from plantas.Trigo import Trigo
from .ISemente import ISemente

class SementeDeTrigo(ISemente):

    def __init__(self, nome='Trigo', preco = 5, caminho_imagem = 'novo_prototipo/assets/ui/sprite_semente_TESTE.png', quantidade = 1):
        super().__init__(nome,
                         preco,
                         caminho_imagem,
                         quantidade)

    def constroi_planta(self, pos, grupo) -> IPlanta:
        planta = Trigo(pos, grupo)
        return planta