import pygame
from Mapa.Blocos.BlocoComInteracao import BlocoComInteracao
from menus.MenuVendedor import MenuVendedor
from entidades.jogador.inventario import Inventario

# Vendedor temporariamente um bloco para MVP

class Vendedor(BlocoComInteracao):
    def __init__(self, x, y, largura, altura, observador):
        super().__init__(x,y,largura,altura,observador, True)
        self.__image = pygame.Surface((self.largura,self.altura))
        self.__image.fill((120,120,120))
        self.__rect = self.__image.get_rect(topleft= (self.x,self.y))
        self.__inventario = Inventario(10)
        self.__imagem = pygame.image.load('novo_prototipo/assets/ui/vendedor_TESTE.png')
        self.__imagem_dialogo = pygame.image.load('novo_prototipo/assets/ui/dialogo_TESTE.png')

    def desenhar(self, tela):
        tela.blit(self.__image, self.__rect)

    def interagir(self, item):
        self.observador.notifica_ativa_menu(MenuVendedor(vendedor=self, caminho_fundo='novo_prototipo/assets/ui/fundo_menu_TESTE.png'))

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
    def inventario(self):
        return self.__inventario
    
    @property
    def imagem_dialogo(self):
        return self.__imagem_dialogo
