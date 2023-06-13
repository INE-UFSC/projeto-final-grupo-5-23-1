import pygame

from entidades.jogador.inventario import Inventario
from itens.ferramentas.Enxada import Enxada
from itens.sementes.SementeDeTrigo import SementeDeTrigo
from settings import LAYERS


class Jogador(pygame.sprite.Sprite):

    def __init__(self, pos, group):
        super().__init__(group)
        self.__z = LAYERS['Entidades']        

        # Setup Geral
        self.__image = pygame.Surface((40,80))
        self.__image.fill('red')
        self.__rect = self.__image.get_rect(midbottom= pos)
        self.__inventario = Inventario(5)

        # Movimentação
        self.__status = 'baixo' # Refere-se a direção que o player está olhando
        self.__posicao = pygame.math.Vector2(self.__rect.midbottom) #Troquei de .center para .midBottom para facilitar o comando de interagir
        self.__velocidade = 200
        self.__item_atual = None

        #Adicição de itens provisória
        self.__inventario.adicionar_item(Enxada('Enxada'))
        self.__inventario.adicionar_item(SementeDeTrigo(quantidade = 10))

        #Comércio
        self.__moedas = 15

    def adiciona_moedas(self, quantidade_de_moedas: int):
        if isinstance(quantidade_de_moedas, int) and quantidade_de_moedas > 0:
            self.__moedas += quantidade_de_moedas

    def remove_moedas(self, quantidade_de_moedas: int):
        if isinstance(quantidade_de_moedas, int) and quantidade_de_moedas > 0:
            self.__moedas -= quantidade_de_moedas

    def seleciona_item(self, item):
        self.__item_atual = item

    def atualiza_status(self, status):
        self.__status = status
        return
    
    def atualiza_posicao(self, posicao):
        
        self.__posicao.x = posicao.x
        self.__posicao.y = posicao.y
        self.__rect.midbottom = posicao
        return

    def update(self):
        if self.__item_atual not in self.__inventario.itens:
            self.__item_atual = None

    def set_inventario(self, inventario):
        self.__inventario = inventario

    @property    
    def status(self):
        return self.__status
    
    @property
    def image(self):
        return self.__image
    
    @property
    def rect(self):
        return self.__rect
    
    @property
    def posicao(self):
        return self.__posicao
    
    @property
    def posicao_matriz(self):
        posicao_matriz = [self.__posicao.x, self.__posicao.y]
        for index, posicao in enumerate(posicao_matriz):
            posicao_matriz[index] = int(posicao // 64)
        return posicao_matriz
    
    @property
    def velocidade(self):
        return self.__velocidade
    
    @property
    def item_atual(self):
        return self.__item_atual
    
    @property
    def inventario(self):
        return self.__inventario
    
    @property
    def moedas(self):
        return self.__moedas

    @property
    def z(self):
         return self.__z