import pygame
from plantas.interfaces.IPlanta import IPlanta
from plantas.Crisalida import Crisalida
from .ISemente import ISemente

class SementeGelada(ISemente):

    def __init__(self, nome='Semente Gelada', preco = 8, caminho_imagem = 'novo_prototipo/assets/ui/sprite_semente_TESTE.png', quantidade = 1):
        super().__init__(nome,
                         preco,
                         caminho_imagem,
                         quantidade)
        self.set_imagem(pygame.Surface((72,72)))
        self.imagem.fill('#afcc33')

    def constroi_planta(self, pos, grupo) -> IPlanta:
        planta = Crisalida(pos, grupo)
        return planta