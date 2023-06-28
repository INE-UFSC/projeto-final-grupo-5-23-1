from itens.ferramentas.Ferramenta import Ferramenta
import os


dir_atual = os.path.dirname(os.path.abspath(__file__))
pasta_assets = os.path.join(dir_atual, '..', '..', 'assets', 'ui')
caminho_imagem = os.path.join(pasta_assets, 'regador_TESTE.png')

class Regador(Ferramenta):

    def __init__(self, nome='Regador', preco=15, caminho_imagem=caminho_imagem):
        super().__init__(nome, preco, caminho_imagem)