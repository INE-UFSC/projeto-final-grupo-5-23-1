import pygame
from itens.ItemQuantizavel import ItemQuantizavel

class CogumeloJade(ItemQuantizavel):

    def __init__(self, nome='Cogumelo Jade', preco=25, caminho_imagem='novo_prototipo/assets/ui/sprite_trigo_TESTE.png', quantidade=1):
        super().__init__(nome, preco, caminho_imagem, quantidade)
        self.set_imagem(pygame.Surface((72,72)))
        self.imagem.fill('#4bb491')