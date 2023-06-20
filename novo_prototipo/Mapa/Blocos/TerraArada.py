import pygame
from Mapa.Blocos.interfaces.IBlocoComInteracao import IBlocoComInteracao
from itens.sementes.ISemente import ISemente
from itens.ferramentas.Regador import Regador
from Mapa.Sobreposicoes.SobreposicaoAgua import SobreposicaoAgua
from plantas.interfaces.IPlanta import IPlanta
from settings import *

class TerraArada(IBlocoComInteracao):
    def __init__(self, pos, surf, groups, observador):
        super().__init__(pos, surf, groups, observador)
        self.__image = pygame.image.load('novo_prototipo/Mapa/Mapas/Tilesets/tileset.png')
        self.__rect = self.__image.get_rect(topleft= pos)
        self.__textura = self.definir_textura()
        self.__z = LAYERS['solo']

        self.__planta = None
        self.__regada = False
        self.__taxa_decaimento_regada = 5
        self.__tempo_restante_regada = 0
        self.__sobreposicao_agua = None

    def adiciona_planta(self, planta: IPlanta):
        if isinstance(planta, IPlanta):
            self.__planta = planta
            self.__planta.adiciona_observador(self)

    def excluir_planta(self):
        self.notifica_exclui_entidade(self.__planta)
        self.__planta = None

    def notifica_plantar(self, semente: ISemente):
        if isinstance(semente, ISemente):
            self.observador.plantar(self.posicao_matriz[0], self.posicao_matriz[1], semente)

    def interagir(self, jogador):
        if isinstance(jogador.item_atual, Regador):
            self.regada = True
            self.__tempo_restante_regada = 5000
            self.__sobreposicao_agua = SobreposicaoAgua(posicao=self.rect.topleft)
            self.notifica_adiciona_entidade(self.__sobreposicao_agua)
            return
        if self.__planta == None:
            if isinstance(jogador.item_atual, ISemente):
                self.notifica_plantar(jogador.item_atual)
        else:
            self.__planta.interagir(jogador)

    def definir_textura(self):
        if self.observador.id == 'Floresta':
            return (64, 0, 64, 64)
        if self.observador.id == 'Deserto':
            return (512, 0, 64, 64)
        if self.observador.id == 'Planicie':
            return (128, 64, 64, 64)
        if self.observador.id == 'Neve':
            return (448, 64, 64, 64)
        if self.observador.id == 'Caverna':
            return (320, 0, 64, 64)

    def draw(self, tela):
        tela.blit(self.__image, self.__rect, self.__textura)

    def update(self):
        if self.__regada:
            self.__tempo_restante_regada -= self.__taxa_decaimento_regada
            if self.__tempo_restante_regada <= 0:
                self.__tempo_restante_regada = 0
                self.__regada = False
                self.notifica_exclui_entidade(self.__sobreposicao_agua)
                self.__sobreposicao_agua = None

    def desenhar(self, tela):
        pass

    @property
    def z(self):
        return self.__z
    
    @property
    def image(self):
        return self.__image
    
    @property
    def rect(self):
        return self.__rect
    
    @property
    def textura(self):
        return self.__textura

    @property
    def regada(self):
        return self.__regada
    
    @regada.setter
    def regada(self, regada: bool):
        self.__regada = regada