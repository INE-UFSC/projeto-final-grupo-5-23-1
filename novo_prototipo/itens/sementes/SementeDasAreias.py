import pygame
from plantas.interfaces.IPlanta import IPlanta
from plantas.PlantaAreia import PlantaAreia
from .ISemente import ISemente

class SementeDasAreias(ISemente):

    def __init__(self, nome='Semente Arenosa', preco = 8, caminho_imagem = 'novo_prototipo/assets/ui/sprite_semente_TESTE.png', quantidade = 1):
        super().__init__(nome,
                         preco,
                         caminho_imagem,
                         quantidade)
        self.set_imagem(pygame.Surface((72,72)))
        self.imagem.fill('#afcc33')

    def constroi_planta(self, pos, grupo) -> IPlanta:
        planta = PlantaAreia(pos, grupo)
        return planta