import pygame
from plantas.interfaces.IPlanta import IPlanta
from plantas.PlantaCaverna import PlantaCaverna
from .ISemente import ISemente

class SementeCaverna(ISemente):

    def __init__(self, nome='Cavernite', preco = 8, caminho_imagem = 'novo_prototipo/assets/ui/sprite_semente_TESTE.png', quantidade = 1):
        super().__init__(nome,
                         preco,
                         caminho_imagem,
                         quantidade)
        self.set_imagem(pygame.Surface((72,72)))
        self.imagem.fill('#e31cc1')

    def constroi_planta(self, pos, grupo, mapa) -> IPlanta:
        planta = PlantaCaverna(pos, grupo, mapa)
        return planta