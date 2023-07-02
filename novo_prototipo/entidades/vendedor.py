import os
import pygame
from Mapa.Blocos.interfaces.IBlocoComInteracao import IBlocoComInteracao
from menus.MenuVendedor import MenuVendedor
from entidades.jogador.inventario import Inventario
from itens.sementes.SementeDaFloresta import SementeDaFloresta
from itens.ferramentas.Enxada import Enxada
from itens.ferramentas.Regador import Regador
from itens.sementes.SementeCogumelo import SementeDeCogumelo
from itens.sementes.SementeDasAreias import SementeDasAreias
from itens.sementes.SementeGelada import SementeGelada
from itens.sementes.SementeCaverna import SementeCaverna
import os

from settings import LAYERS


dir_atual = os.path.dirname(os.path.abspath(__file__))
pasta_assets = os.path.join(dir_atual, '..', 'assets', 'ui')
caminho_sprite = os.path.join(pasta_assets, 'sprite_vendedor.png')

class Vendedor(IBlocoComInteracao):
    def __init__(self, pos, surf, groups, observador, mapa):
        super().__init__(pos, surf, groups, observador, True)
        self.__image = pygame.transform.scale(pygame.image.load(caminho_sprite), (64*2, 64*2))
        self.__hitbox = pygame.Surface((64,64)).get_rect(topleft= pos)
        self.__rect = self.__image.get_rect(midbottom= self.hitbox.midbottom)
        self.__mapa = mapa
        
        self.__inventario = Inventario([4,5])
        self.z = LAYERS['main']

        #Atributos personalidade:
        if self.__mapa == 'Floresta':
            self.__nome = 'Halley, a "viajante"'
            self.__inventario.adicionar_item(SementeDaFloresta(quantidade = 10))
            self.__inventario.adicionar_item(SementeDeCogumelo())
            self.__inventario.adicionar_item(SementeDasAreias())
            self.__inventario.adicionar_item(SementeCaverna())
            self.__inventario.adicionar_item(SementeGelada())
            self.__inventario.adicionar_item(Enxada())
            self.__inventario.adicionar_item(Regador())
        
        if self.__mapa == 'Deserto':
            self.__nome = 'Halley, a "viajante"'
            self.__inventario.adicionar_item(SementeDasAreias(preco= 20,quantidade= 20))
        
        if self.__mapa == 'Planicie':
            self.__nome = 'Halley, a "viajante"'
            self.__inventario.adicionar_item(SementeDeCogumelo(quantidade= 20, preco= 10))
        
        if self.__mapa == 'Neve':
            self.__nome = 'Halley, a "viajante"'
            self.__inventario.adicionar_item(SementeGelada(quantidade= 15))
        
        if self.__mapa == 'Caverna':
            self.__nome = 'Halley, a "viajante"'
            self.__inventario.adicionar_item(SementeCaverna(quantidade= 3))

        if self.__mapa == 'Transporte':
            self.__nome = 'Halley, a "viajante"'

        self.__dir_atual = os.path.dirname(os.path.abspath(__file__))
        self.__pasta_assets = os.path.join(self.__dir_atual, '..', 'assets', 'ui')
        self.__caminho_imagem_vendedor = os.path.join(self.__pasta_assets, 'vendedor.png')
        self.__caminho_dialogo_vendedor = os.path.join(self.__pasta_assets, 'dialogo_TESTE.png')
        self.__caminho_fundo_menu_vendedor = os.path.join(self.__pasta_assets, 'fundo_menu.png')
        self.__caminho_seta = os.path.join(self.__pasta_assets, 'seta_TESTE.png')

        self.__imagem = pygame.transform.scale(pygame.image.load(self.__caminho_imagem_vendedor), (320, 310))
        self.__imagem_dialogo = pygame.image.load(self.__caminho_dialogo_vendedor)

    def desenhar(self, tela):
        tela.blit(self.__image, self.__rect)

    def interagir(self, jogador):
        self.observador.notifica_ativa_menu(MenuVendedor(vendedor=self,
                                                         caminho_fundo=self.__caminho_fundo_menu_vendedor,
                                                         caminho_seta=self.__caminho_seta,
                                                         jogador=jogador))

    @property
    def rect(self):
        return self.__rect
    
    @property
    def image(self):
        return self.__image
    
    @property
    def imagem(self):
        return self.__imagem
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def inventario(self):
        return self.__inventario
    
    @property
    def imagem_dialogo(self):
        return self.__imagem_dialogo

    @property
    def hitbox(self):
        return self.__hitbox