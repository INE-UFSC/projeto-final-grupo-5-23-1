from itens.ItemQuantizavel import ItemQuantizavel
import os


dir_atual = os.path.dirname(os.path.abspath(__file__))
pasta_assets = os.path.join(dir_atual, '..', '..', 'assets', 'ui')
caminho_imagem = os.path.join(pasta_assets, 'fruto_amarelo.png')

class FrutoAreia(ItemQuantizavel):

    def __init__(self, nome='Pégaso', preco=25, caminho_imagem=caminho_imagem, quantidade=1):
        super().__init__(nome, preco, caminho_imagem, quantidade)