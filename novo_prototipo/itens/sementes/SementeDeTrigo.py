from plantas.interfaces.IPlanta import IPlanta
from plantas.Trigo import Trigo
from .ISemente import ISemente
import os


dir_atual = os.path.dirname(os.path.abspath(__file__))
pasta_assets = os.path.join(dir_atual, '..', '..', 'assets', 'ui')
caminho_imagem = os.path.join(pasta_assets, 'sprite_semente_TESTE.png')

class SementeDeTrigo(ISemente):

    def __init__(self, nome='Trigo', preco = 5, caminho_imagem = caminho_imagem, quantidade = 1):
        super().__init__(nome,
                         preco,
                         caminho_imagem,
                         quantidade)

    def constroi_planta(self, pos, grupo) -> IPlanta:
        planta = Trigo(pos, grupo)
        return planta