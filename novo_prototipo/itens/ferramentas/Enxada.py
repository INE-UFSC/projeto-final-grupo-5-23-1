from .Ferramenta import Ferramenta
import os


dir_atual = os.path.dirname(os.path.abspath(__file__))
pasta_assets = os.path.join(dir_atual, '..', '..', 'assets', 'ui')
caminho_imagem = os.path.join(pasta_assets, 'enxada_TESTE.png')

class Enxada(Ferramenta):

    def __init__(self, nome='Enxada', preco = 10, caminho_imagem = caminho_imagem):
        super().__init__(nome, preco, caminho_imagem)