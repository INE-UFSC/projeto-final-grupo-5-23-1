import pygame
from Mapa.Bloco import Bloco
from entidades.jogador.jogador import Jogador

class BlocoDeGrama(Bloco):
    def __init__(self, x, y, largura, altura):
        super().__init__(x, y, largura, altura)
        self.arado = False
        self.cor = (0, 64, 0) 

    def desenhar(self, tela):
        pygame.draw.rect(tela, self.cor, (self.x, self.y, self.largura, self.altura))

    def arar_terra(self, jogador):
        if not self.arado and jogador.ferramenta_atual == 'enxada':
            self.arado = True
            self.cor = (139, 69, 19) 

