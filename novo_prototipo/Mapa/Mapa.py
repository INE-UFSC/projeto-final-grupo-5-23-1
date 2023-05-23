from pygame import Surface, Vector2
import pygame
from Mapa.Blocos.Grama import BlocoDeGrama
from Mapa.Blocos.agua import Agua
from Mapa.interfaces.IMapa import IMapa
from entidades.jogador.jogador import Jogador
from entidades.vendedor import Vendedor
from plantas.Planta import Planta

class Mapa(IMapa):
    def __init__(self):
        self.__id = 'campo'
        self.__blocos = []
        self.__entidades = []
        self.__grupoJogador = pygame.sprite.Group()
        self.__grupoEntidades = pygame.sprite.Group()
        self.__grupoPlantas = pygame.sprite.Group()
        self.construir_blocos()
        self.adiciona_entidades()

    @property
    def plantas(self):
        return self.__grupoPlantas.sprites()
    
    @property
    def blocos(self):
        return self.__blocos
    
    @blocos.setter
    def blocos(self, blocos):
        self.__blocos = blocos
        return
    
    @property
    def id(self):
        return self.__id
    
    @property
    def jogador(self):
        return self.__entidades[0]
    
    def troca_bloco(self, posicao_x_matriz, posicao_y_matriz, novo_bloco):
        self.__blocos[posicao_y_matriz][posicao_x_matriz] = novo_bloco
        return
    
    def plantar(self, posicao_x_matriz, posicao_y_matriz, item):
        posicao_planta = Vector2()
        posicao_planta.x = self.__blocos[posicao_y_matriz][posicao_x_matriz].x + 32
        posicao_planta.y = self.__blocos[posicao_y_matriz][posicao_x_matriz].y + 40
        planta = Planta(item.planta_a_ser_gerada, posicao_planta, self.__grupoPlantas)
        self.__blocos[posicao_y_matriz][posicao_x_matriz].adiciona_planta(planta)
        self.jogador.inventario.remover_item(item)

    def construir_blocos(self):
        largura_bloco = 64
        altura_bloco = 64
        qtd_blocos_x = 768 // largura_bloco
        qtd_blocos_y = 1280 // altura_bloco
        
        for x in range(qtd_blocos_x):
            linha = []
            for y in range(qtd_blocos_y):
                if x == 2 and y == 2:
                    bloco = Vendedor(y*largura_bloco, x*altura_bloco, largura_bloco, altura_bloco, self)
                elif y == 0 or y == qtd_blocos_y -1 or x == 0 or x == qtd_blocos_x - 1:
                    bloco = Agua(y*largura_bloco, x*altura_bloco, largura_bloco, altura_bloco, self)
                else:
                    bloco = BlocoDeGrama(y * largura_bloco, x * altura_bloco, largura_bloco, altura_bloco, self)
                linha.append(bloco)
            self.blocos.append(linha)

    def adiciona_entidades(self):
        self.__entidades.append(Jogador((640,360), self.__grupoJogador))

    def desenhar(self, tela: Surface):
        for linha in (self.blocos):
            for bloco in linha:
                bloco.desenhar(tela)
        self.__grupoPlantas.draw(tela)
        self.__grupoJogador.draw(tela)
