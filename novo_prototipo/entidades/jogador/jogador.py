import pygame

from entidades.jogador.inventario import Inventario
from itens.ferramentas.Enxada import Enxada
from itens.sementes.Semente1 import Semente1
from comandos.ComandoMover import ComandoMover


class Jogador(pygame.sprite.Sprite):

    #[TODO] - Refatorar o inventario

    def __init__(self, pos, group, grupoBlocos):
        super().__init__(group)

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
        self.__inventario.adicionar_item(Enxada('Enxada de madeira'))
        self.__inventario.adicionar_item(Semente1('Trigo', 10))

        # Comando de Movimento
        self.__comando_mover = None
        self.__grupoBlocos = grupoBlocos
        self.__delta_tempo = 0        

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