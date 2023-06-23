import pygame
from itens.recursos.Luxiaria import Luxiaria
from itens.Item import Item

from plantas.interfaces.IPlanta import IPlanta

class PlantaCaverna(IPlanta):

    def __init__(self, pos, grupo):
        super().__init__(nome='Crisalida', pos=pos, grupo=grupo)
        #Trocar por uma classe que lidará com as sprites depois:
        self.__image = pygame.Surface((5,15))
        self.__image.fill('#2737d8')
        self.__rect = self.__image.get_rect(midbottom=pos)
        
        #--------------------------------------------------------
         # Tempo de crescimento dos estágios
        self.temposBase = [15.0, 40.0]
        self.temposRegada = [20.0, 50.0]

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
            self.__image = pygame.Surface((20,10))
            self.__image.fill('#e8ad17')
            
        elif self.temposAtuais[0] < segundos < self.temposAtuais[1]:
            self.__image = pygame.Surface((15,30))
            self.__image.fill('#d52a2c')

        elif segundos >= self.temposAtuais[1]:
            self.__image = pygame.Surface((15,70))
            self.__image.fill('#d02f7d')
            self.em_crescimento = False
        
        self.__rect = self.__image.get_rect(midbottom = posicao_antiga)


    def interagir(self, jogador):
        if not self.em_crescimento:
            lista_nomes_itens = []
            for item in jogador.inventario.itens:
                if isinstance(item, Item):
                    lista_nomes_itens.append(item.nome)
            item = Luxiaria()
            if (jogador.inventario.capacidade_atual < jogador.inventario.capacidade_maxima) or (item.nome in  lista_nomes_itens):
                jogador.inventario.adicionar_item(item)
                self.notifica_exclui_planta()