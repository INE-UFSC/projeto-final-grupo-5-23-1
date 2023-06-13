from itens.ItemQuantizavel import ItemQuantizavel


class FardoDeTrigo(ItemQuantizavel):

    def __init__(self, nome='Fardo de Trigo', preco=10, caminho_imagem='novo_prototipo/assets/ui/sprite_trigo_TESTE.png', quantidade=1):
        super().__init__(nome, preco, caminho_imagem, quantidade)