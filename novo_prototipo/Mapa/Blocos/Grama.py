import pygame
from Mapa.Blocos.BlocoComInteracao import BlocoComInteracao
from Mapa.Blocos.TerraArada import TerraArada
from itens.ferramentas.Enxada import Enxada

class BlocoDeGrama(BlocoComInteracao):
    def __init__(self, pos, surf, groups, observador):
        super().__init__(pos, surf, groups, observador)
    
    def interagir(self, item):
        if isinstance(item, Enxada):
            self.notifica_troca_bloco(self.posicao_matriz[0], self.posicao_matriz[1], TerraArada(self.x, self.y, self.largura, self.altura, self.observador))
    
    def desenhar(self):
        pass