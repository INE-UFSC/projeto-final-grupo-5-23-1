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
         # Tempo de crescimento dos estágios
        self.nascimento = pygame.time.get_ticks()

        self.baseTempoEstagio1 = 3.0
        self.baseTempoCrescido = 10.0

        self.tempoEstagio1 = 3.0
        self.tempoCrescido = 10.0

        #--------------------------------------------------------
        
    @property
    def image(self):
        return self.__image
    
    @property
    def rect(self):
        return self.__rect
    
    
    def atualiza_tempos(self):
        if self.observadores[0].regada:
            self.tempoEstagio1 = self.baseTempoEstagio1 * 0.75
            self.tempoCrescido = self.baseTempoCrescido * 0.75
        else:
            self.tempoEstagio1 = self.baseTempoEstagio1
            self.tempoCrescido = self.baseTempoCrescido
    
    def atualiza_sprite(self):
        posicao_antiga = self.__rect.midbottom
        self.agora = pygame.time.get_ticks()
        segundos = self.calcular_segundos()
        if segundos < self.tempoEstagio1:
            self.__image = pygame.Surface((5,10))
            self.__image.fill('saddlebrown')
        elif self.tempoEstagio1 < segundos < self.tempoCrescido:
            self.__image = pygame.Surface((10,40))
            self.__image.fill('chartreuse')
        elif segundos >= self.tempoCrescido:
            self.__image = pygame.Surface((20,80))
            self.__image.fill('yellow')
            self.em_crescimento = False
        self.__rect = self.__image.get_rect(midbottom = posicao_antiga)
    
    def calcular_segundos(self):
        return (self.agora - self.nascimento) / 1000
    
    def update(self):
        self.atualiza_tempos()
        if self.em_crescimento:
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