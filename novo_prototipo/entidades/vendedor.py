import os
import pygame
from Mapa.Blocos.interfaces.IBlocoComInteracao import IBlocoComInteracao
from menus.MenuVendedor import MenuVendedor
from entidades.jogador.inventario import Inventario
from itens.sementes.SementeDeTrigo import SementeDeTrigo
from itens.ferramentas.Enxada import Enxada
from itens.ferramentas.Regador import Regador
from itens.sementes.SementeCogumelo import SementeDeCogumelo
from itens.sementes.SementeDasAreias import SementeDasAreias
from itens.sementes.SementeGelada import SementeGelada
from itens.sementes.SementeCaverna import SementeCaverna

class Vendedor(IBlocoComInteracao):
    def __init__(self, pos, surf, groups, observador, mapa):
        super().__init__(pos, surf, groups, observador, True)
        self.__image = pygame.Surface((64,64))
        self.__image.fill((120,120,120))
        self.__rect = self.__image.get_rect(topleft= pos)
        self.__mapa = mapa
        
        self.__inventario = Inventario([4,5])

        #Atributos personalidade:
        if self.__mapa == 'Floresta':
            self.__nome = "Flofler, a vendedora"
            self.__inventario.adicionar_item(SementeDeTrigo(nome = 'Trigo', quantidade = 10))
            self.__inventario.adicionar_item(Enxada('Enxada'))
            self.__inventario.adicionar_item(SementeDeTrigo(nome = 'Trigo2', quantidade = 10))
            self.__inventario.adicionar_item(SementeDeTrigo(nome = 'Trigo3', quantidade = 10))
            self.__inventario.adicionar_item(SementeDeTrigo(nome = 'Trigo4', quantidade = 10))
            self.__inventario.adicionar_item(SementeDeTrigo(nome = 'Trigo5', quantidade = 10))
            self.__inventario.adicionar_item(SementeDeTrigo(nome = 'Trigo6', quantidade = 10))
            self.__inventario.adicionar_item(SementeDeTrigo(nome = 'Trigo7', quantidade = 10))
            self.__inventario.adicionar_item(SementeDeTrigo(nome = 'Trigo8', quantidade = 10))
            self.__inventario.adicionar_item(SementeDeTrigo(nome = 'Trigo9', quantidade = 10))
            self.__inventario.adicionar_item(SementeDeTrigo(nome = 'Trigo10', quantidade = 10))
        
        if self.__mapa == 'Deserto':
            self.__nome = "Bolt, o supercão"
            self.__inventario.adicionar_item(SementeDasAreias(nome= 'Semente Arenosa', preco= 20,quantidade= 20))
        
        if self.__mapa == 'Planicie':
            self.__nome = "Power Ranger Rosa"
            self.__inventario.adicionar_item(SementeDeCogumelo(nome='Cogumelo Jade', quantidade= 20, preco= 10))
        
        if self.__mapa == 'Neve':
            self.__nome = "SaNs UndERtaLe"
            self.__inventario.adicionar_item(SementeGelada(nome= 'Semente Gelada', quantidade= 15))
        
        if self.__mapa == 'Caverna':
            self.__nome = "The Princess is in another castle"
            self.__inventario.adicionar_item(SementeCaverna(nome='Cavernite', quantidade= 3))

        if self.__mapa == 'Transporte':
            self.__nome = 'Michael Jackson'

        self.__dir_atual = os.path.dirname(os.path.abspath(__file__))
        self.__pasta_assets = os.path.join(self.__dir_atual, '..', 'assets', 'ui')
        self.__caminho_imagem_vendedor = os.path.join(self.__pasta_assets, 'vendedor_TESTE.png')
        self.__caminho_dialogo_vendedor = os.path.join(self.__pasta_assets, 'dialogo_TESTE.png')
        self.__caminho_fundo_menu_vendedor = os.path.join(self.__pasta_assets, 'fundo_menu_TESTE.png')
        self.__caminho_seta = os.path.join(self.__pasta_assets, 'seta_TESTE.png')

        self.__imagem = pygame.image.load(self.__caminho_imagem_vendedor)
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
