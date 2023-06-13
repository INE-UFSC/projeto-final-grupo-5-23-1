from .Ferramenta import Ferramenta

class Enxada(Ferramenta):

    def __init__(self, nome='Enxada', preco = 10, caminho_imagem = 'novo_prototipo/assets/ui/enxada_TESTE.png'):
        super().__init__(nome, preco, caminho_imagem)