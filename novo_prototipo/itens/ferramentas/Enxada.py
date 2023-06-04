from .Ferramenta import Ferramenta

class Enxada(Ferramenta):

    def __init__(self, nome, preco = 10, caminho_imagem = 'novo_prototipo/assets/ui/sprite_enxada_minecraft_TESTE.png'):
        super().__init__(nome, preco, caminho_imagem)