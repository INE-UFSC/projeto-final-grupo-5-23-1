import pygame
from plantas.interfaces.IPlanta import IPlanta
from plantas.Cogumelo import Cogumelo
from .ISemente import ISemente

class SementeDeCogumelo(ISemente):

    def __init__(self, nome='Cogumelo', preco = 10, caminho_imagem = 'novo_prototipo/assets/ui/sprite_semente_TESTE.png', quantidade = 1):
        super().__init__(nome,
                         preco,
                         caminho_imagem,
                         quantidade)
        self.set_imagem(pygame.Surface((72,72)))
        self.imagem.fill('#c0403f')

    def constroi_planta(self, pos, grupo) -> IPlanta:
        planta = Cogumelo(pos, grupo)
        return planta