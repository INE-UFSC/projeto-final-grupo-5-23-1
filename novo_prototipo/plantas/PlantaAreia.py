import pygame
from itens.recursos.FrutoAreia import FrutoAreia
from itens.Item import Item

from plantas.interfaces.IPlanta import IPlanta

class PlantaAreia(IPlanta):

    def __init__(self, pos, grupo):
        super().__init__(nome='Planta da Areia', pos=pos, grupo=grupo)
        #Trocar por uma classe que lidará com as sprites depois:
        self.__image = pygame.Surface((10,15))
        self.__image.fill('#48b753')
        self.__rect = self.__image.get_rect(midbottom=pos)

        #--------------------------------------------------------
         # Tempo de crescimento dos estágios
        self.temposBase = [4.5,15.0]
        self.temposRegada = [10.0, 30.0]

        self.temposAtuais = self.temposBase
        #--------------------------------------------------------
        
    @property
    def image(self):
        return self.__image
    
    @property
    def rect(self):
        return self.__rect

    def atualiza_sprite(self):
        posicao_antiga = self.__rect.midbottom
        self.agora = pygame.time.get_ticks()
        segundos = self.calcular_segundos()

        if segundos < self.temposAtuais[0]:
            self.__image = pygame.Surface((10,10))
            self.__image.fill('#48b753')
            
        elif self.temposAtuais[0] < segundos < self.temposAtuais[1]:
            self.__image = pygame.Surface((25,12))
            self.__image.fill('#42bd8e')

        elif segundos >= self.temposAtuais[1]:
            self.__image = pygame.Surface((40,30))
            self.__image.fill('#2fd0d0')
            self.em_crescimento = False
        
        self.__rect = self.__image.get_rect(midbottom = posicao_antiga)

    def interagir(self, jogador):
        if not self.em_crescimento:
            lista_nomes_itens = []
            for item in jogador.inventario.itens:
                if isinstance(item, Item):
                    lista_nomes_itens.append(item.nome)
            item = FrutoAreia()
            if (jogador.inventario.capacidade_atual < jogador.inventario.capacidade_maxima) or (item.nome in  lista_nomes_itens):
                jogador.inventario.adicionar_item(item)
                self.notifica_exclui_planta()

    def multiplicador_clima(self):
        if self.clima == 'Floresta':
            multiplicador = 1
        elif self.clima == 'Deserto':
            multiplicador = 1.5
        elif self.clima == 'Caverna':
            multiplicador = 2
        elif self.clima == 'Neve':
            multiplicador = 1.2
        elif self.clima == 'Planicie':
            multiplicador = 1
        else:
            multiplicador = 1
        return multiplicador