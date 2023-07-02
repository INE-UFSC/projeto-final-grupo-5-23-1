import pygame
from Mapa.Blocos.interfaces.IBlocoComInteracao import IBlocoComInteracao
from Mapa.Blocos.TerraArada import TerraArada
from itens.ferramentas.Enxada import Enxada

class BlocoDeGrama(IBlocoComInteracao):
    def __init__(self, pos, surf, groups, observador, manual=False):
        super().__init__(pos, surf, groups, observador)
        self.__groups = groups
        self.__manual = manual

        if self.__manual:
            self.image = pygame.image.load('novo_prototipo/Mapa/Mapas/Tilesets/tileset.png')
            self.rect = self.image.get_rect(topleft= pos)
            self.textura = self.definir_textura()
    
    def definir_textura(self):
        if self.observador.id == 'Floresta':
            return (0, 0, 64, 64)
        if self.observador.id == 'Deserto':
            return (256, 0, 64, 64)
        if self.observador.id == 'Planicie':
            return (64, 64, 64, 64)
        if self.observador.id == 'Neve':
            return (576, 0, 64, 64)
        if self.observador.id == 'Caverna':
            return (320, 64, 64, 64)
    
    def interagir(self, jogador):
        if isinstance(jogador.item_atual, Enxada):
            bloco = TerraArada(self.pos, self.surf, [self.observador.grupoAll, self.observador.grupoBlocos], self.observador, self)
            self.notifica_troca_bloco(self.posicao_matriz[0], self.posicao_matriz[1], bloco)

    def draw(self, tela):
        if self.__manual:
            tela.blit(self.image, self.rect, self.textura)
        else:
            super().draw()