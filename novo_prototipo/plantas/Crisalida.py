import pygame
from itens.recursos.Criofru import Criofru
from itens.Item import Item

from plantas.interfaces.IPlanta import IPlanta

class Crisalida(IPlanta):

    def __init__(self, pos, grupo, mapa):
        super().__init__(mapa=mapa,nome='Crisalida', pos=pos, grupo=grupo)
        #Trocar por uma classe que lidará com as sprites depois:
        self.__image = pygame.Surface((5,15))
        self.__image.fill('#2737d8')
        self.__rect = self.__image.get_rect(midbottom=pos)
        
        #--------------------------------------------------------
         # Tempo de crescimento dos estágios
        self.temposBase = [12.0, 32.0]
        self.temposRegada = [9.0, 24.0]

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
            self.__image = pygame.Surface((5,15))
            self.__image.fill('#2737d8')
            
        elif self.temposAtuais[0] < segundos < self.temposAtuais[1]:
            self.__image = pygame.Surface((10,35))
            self.__image.fill('#6e34cb')

        elif segundos >= self.temposAtuais[1]:
            self.__image = pygame.Surface((20,45))
            self.__image.fill('#bd2cd3')
            self.em_crescimento = False
        
        self.__rect = self.__image.get_rect(midbottom = posicao_antiga)


    def interagir(self, jogador):
        if not self.em_crescimento:
            lista_nomes_itens = []
            for item in jogador.inventario.itens:
                if isinstance(item, Item):
                    lista_nomes_itens.append(item.nome)
            item = Criofru()
            if (jogador.inventario.capacidade_atual < jogador.inventario.capacidade_maxima) or (item.nome in  lista_nomes_itens):
                jogador.inventario.adicionar_item(item)
                self.notifica_exclui_planta()