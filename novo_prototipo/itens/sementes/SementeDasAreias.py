import pygame
from plantas.interfaces.IPlanta import IPlanta
from plantas.PlantaAreia import PlantaAreia
from .ISemente import ISemente
import os


dir_atual = os.path.dirname(os.path.abspath(__file__))
pasta_assets = os.path.join(dir_atual, '..', '..', 'assets', 'ui')
caminho_imagem = os.path.join(pasta_assets, 'semente_amarela.png')

class SementeDasAreias(ISemente):

    def __init__(self, nome='Semente Arenosa', preco = 8, caminho_imagem = caminho_imagem, quantidade = 1):
        super().__init__(nome,
                         preco,
                         caminho_imagem,
                         quantidade)

    def constroi_planta(self, pos, grupo) -> IPlanta:
        planta = PlantaAreia(pos, grupo)
        return planta