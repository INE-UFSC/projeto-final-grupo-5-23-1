import pygame
from Mapa.Blocos.BlocoComInteracao import BlocoComInteracao
from menus.MenuVendedor import MenuVendedor
from entidades.jogador.inventario import Inventario
from itens.sementes.Semente1 import Semente1
from itens.ferramentas.Enxada import Enxada

# Vendedor temporariamente um bloco para MVP

class Vendedor(BlocoComInteracao):
    def __init__(self, x, y, largura, altura, observador):
        super().__init__(x,y,largura,altura,observador, True)
        self.__image = pygame.Surface((self.largura,self.altura))
        self.__image.fill((120,120,120))
        self.__rect = self.__image.get_rect(topleft= (self.x,self.y))
        
        #Atributos personalidade:
        self.__nome = "Flofler, a vendedora"
        self.__inventario = Inventario(20)
        self.__inventario.adicionar_item(Semente1(nome = 'Trigo', quantidade = 10))
        self.__inventario.adicionar_item(Enxada('Enxada'))
        self.__inventario.adicionar_item(Semente1(nome = 'Trigo2', quantidade = 10))
        self.__inventario.adicionar_item(Semente1(nome = 'Trigo3', quantidade = 10))
        self.__inventario.adicionar_item(Semente1(nome = 'Trigo4', quantidade = 10))
        self.__inventario.adicionar_item(Semente1(nome = 'Trigo5', quantidade = 10))
        self.__inventario.adicionar_item(Semente1(nome = 'Trigo6', quantidade = 10))
        self.__inventario.adicionar_item(Semente1(nome = 'Trigo7', quantidade = 10))
        self.__inventario.adicionar_item(Semente1(nome = 'Trigo8', quantidade = 10))
        self.__inventario.adicionar_item(Semente1(nome = 'Trigo9', quantidade = 10))
        self.__inventario.adicionar_item(Semente1(nome = 'Trigo10', quantidade = 10))
        self.__imagem = pygame.image.load('novo_prototipo/assets/ui/vendedor_TESTE.png')
        self.__imagem_dialogo = pygame.image.load('novo_prototipo/assets/ui/dialogo_TESTE.png')

    def desenhar(self, tela):
        tela.blit(self.__image, self.__rect)

    def interagir(self, jogador):
        self.observador.notifica_ativa_menu(MenuVendedor(vendedor=self, caminho_fundo='novo_prototipo/assets/ui/fundo_menu_TESTE.png',caminho_seta='novo_prototipo/assets/ui/seta_TESTE.png', jogador=jogador))

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
