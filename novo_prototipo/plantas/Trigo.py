import pygame
from itens.recursos.FardoDeTrigo import FardoDeTrigo

from plantas.interfaces.IPlanta import IPlanta

class Trigo(IPlanta):

    def __init__(self, pos, grupo):
        super().__init__(nome='Trigo', pos=pos, grupo=grupo)
        #Trocar por uma classe que lidará com as sprites depois:
        self.__image = pygame.Surface((10,10))
        self.__image.fill('saddlebrown')
        self.__rect = self.__image.get_rect(midbottom=pos)
        #--------------------------------------------------------
        self.__taxa_de_crescimento = 10
        self.__progresso_crescimento = 0
        

    @property
    def image(self):
        return self.__image
    
    @property
    def rect(self):
        return self.__rect
    
    def update(self):
        if self.em_crescimento:
            self.__progresso_crescimento +=  self.__taxa_de_crescimento
            posicao_antiga = self.__rect.midbottom
            if self.__progresso_crescimento < 1000:
                self.__image = pygame.Surface((5,10))
                self.__image.fill('saddlebrown')
            elif self.__progresso_crescimento < 2000: 
                self.__image = pygame.Surface((10,40))
                self.__image.fill('chartreuse')
            elif self.__progresso_crescimento < 4000:
                self.__image = pygame.Surface((20,80))
                self.__image.fill('yellow')
                self.em_crescimento = False
            self.__rect = self.__image.get_rect(midbottom = posicao_antiga)

    def interagir(self, jogador):
        if not self.em_crescimento:
            jogador.inventario.adicionar_item(FardoDeTrigo())
            self.notifica_exclui_planta()
