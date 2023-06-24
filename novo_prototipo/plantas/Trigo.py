import pygame
from itens.recursos.FardoDeTrigo import FardoDeTrigo
from itens.Item import Item

from plantas.interfaces.IPlanta import IPlanta

class Trigo(IPlanta):

    def __init__(self, pos, grupo, mapa):
        super().__init__(mapa=mapa,nome='Trigo', pos=pos, grupo=grupo)
        #Trocar por uma classe que lidará com as sprites depois:
        self.__image = pygame.Surface((10,10))
        self.__image.fill('saddlebrown')
        self.__rect = self.__image.get_rect(midbottom=pos)
        
        #--------------------------------------------------------
         # Tempo de crescimento dos estágios
        self.temposBase = [3.0,10.0]
        self.temposRegada = [2.25, 7.5]

        self.temposAtuais = self.temposBase
        #--------------------------------------------------------
        
    @property
    def image(self):
        return self.__image
    
    @property
    def rect(self):
        return self.__rect
    
    def multiplicador_mapa(self):
        multiplicador = 0
        if self.mapa == 'Floresta':
            multiplicador = 1
        elif self.mapa == 'Deserto':
            multiplicador = 1.5
        elif self.mapa == 'Caverna':
            multiplicador = 2
        elif self.mapa == 'Neve':
            multiplicador = 1.2
        elif self.mapa == 'Planicie':
            multiplicador = 1
        else:
            multiplicador = 1
        return multiplicador

    def atualiza_sprite(self):
        posicao_antiga = self.__rect.midbottom
        self.agora = pygame.time.get_ticks()
        segundos = self.calcular_segundos()

        if segundos < self.temposAtuais[0]:
            self.__image = pygame.Surface((5,10))
            self.__image.fill('saddlebrown')
            
        elif self.temposAtuais[0] < segundos < self.temposAtuais[1]:
            self.__image = pygame.Surface((10,40))
            self.__image.fill('chartreuse')

        elif segundos >= self.temposAtuais[1]:
            self.__image = pygame.Surface((20,80))
            self.__image.fill('yellow')
            self.em_crescimento = False
        
        self.__rect = self.__image.get_rect(midbottom = posicao_antiga)


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