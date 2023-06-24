import pygame
from itens.recursos.CogumeloJade import CogumeloJade
from itens.Item import Item

from plantas.interfaces.IPlanta import IPlanta

class Cogumelo(IPlanta):

    def __init__(self, pos, grupo, mapa):
        super().__init__(mapa=mapa, nome='Cogumelo Jade', pos=pos, grupo=grupo)
        #Trocar por uma classe que lidará com as sprites depois:
        self.__image = pygame.Surface((10,15))
        self.__image.fill('beige')
        self.__rect = self.__image.get_rect(midbottom=pos)

        #--------------------------------------------------------
         # Tempo de crescimento dos estágios
        self.temposBase = [10.0,25.0]
        self.temposRegada = [8.0, 20.0]

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
            self.__image = pygame.Surface((10,15))
            self.__image.fill('beige')
            
        elif self.temposAtuais[0] < segundos < self.temposAtuais[1]:
            self.__image = pygame.Surface((15,30))
            self.__image.fill('#e2fef4')

        elif segundos >= self.temposAtuais[1]:
            self.__image = pygame.Surface((40,60))
            self.__image.fill('#78ffce')
            self.em_crescimento = False
        
        self.__rect = self.__image.get_rect(midbottom = posicao_antiga)

    def interagir(self, jogador):
        if not self.em_crescimento:
            lista_nomes_itens = []
            for item in jogador.inventario.itens:
                if isinstance(item, Item):
                    lista_nomes_itens.append(item.nome)
            item = CogumeloJade()
            if (jogador.inventario.capacidade_atual < jogador.inventario.capacidade_maxima) or (item.nome in  lista_nomes_itens):
                jogador.inventario.adicionar_item(item)
                self.notifica_exclui_planta()
