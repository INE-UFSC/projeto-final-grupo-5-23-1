import pygame
from Mapa.Blocos.BlocoComInteracao import BlocoComInteracao
from Mapa.Blocos.TerraArada import TerraArada

class BlocoDeGrama(BlocoComInteracao):
    def __init__(self, x, y, largura, altura, observador):
        super().__init__(x, y, largura, altura, observador)
    
    def interagir(self, item):
        if item == 'enxada':
            self.notifica_troca_bloco(self.posicao_matriz[0], self.posicao_matriz[1], TerraArada(self.x, self.y, self.largura, self.altura, self.observador))
        
    def desenhar(self, tela):
        pygame.draw.rect(tela, (0, 64, 0), (self.x, self.y, self.largura, self.altura))