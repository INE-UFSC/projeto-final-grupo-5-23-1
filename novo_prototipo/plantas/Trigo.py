import pygame
from itens.recursos.FardoDeTrigo import FardoDeTrigo
from itens.Item import Item

from plantas.interfaces.IPlanta import IPlanta

class Trigo(IPlanta):

    def __init__(self, pos, grupo):
        super().__init__(nome='Trigo', pos=pos, grupo=grupo)
        #Trocar por uma classe que lidará com as sprites depois:
        self.__image = pygame.Surface((10,10))
        self.__image.fill('saddlebrown')
        self.__rect = self.__image.get_rect(midbottom=pos)
        #--------------------------------------------------------
        self.taxa_de_crescimento = 10
        self.taxa_de_crescimento_base = 10
        self.progresso_crescimento = 0
        
    @property
    def image(self):
        return self.__image
    
    @property
    def rect(self):
        return self.__rect
    
    
    def atualiza_taxa_de_crescimento(self):
        if self.observadores[0].regada:
            self.taxa_de_crescimento = 50
        else:
            self.taxa_de_crescimento = self.taxa_de_crescimento_base
    
    def atualiza_sprite(self):
        posicao_antiga = self.__rect.midbottom
        if self.progresso_crescimento < 1000:
            self.__image = pygame.Surface((5,10))
            self.__image.fill('saddlebrown')
        elif self.progresso_crescimento < 2000: 
            self.__image = pygame.Surface((10,40))
            self.__image.fill('chartreuse')
        elif self.progresso_crescimento >= 4000:
            self.__image = pygame.Surface((20,80))
            self.__image.fill('yellow')
            self.em_crescimento = False
        self.__rect = self.__image.get_rect(midbottom = posicao_antiga)
    
    def update(self):
        self.atualiza_taxa_de_crescimento()
        if self.em_crescimento:
            self.progresso_crescimento +=  self.taxa_de_crescimento
            self.atualiza_sprite()

    def interagir(self, jogador):
        if not self.em_crescimento:
            lista_nomes_itens = []
            for item in jogador.inventario.itens:
                if isinstance(item, Item):
                    lista_nomes_itens.append(item.nome)
            item = FardoDeTrigo()
            if (jogador.inventario.capacidade_atual < jogador.inventario.capacidade_maxima) or (item.nome in  lista_nomes_itens):
                jogador.inventario.adicionar_item(item)
                self.notifica_exclui_planta()
