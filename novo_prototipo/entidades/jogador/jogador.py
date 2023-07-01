import os
import pygame
from TabelaSprite import TabelaSprite
from settings import *

from entidades.jogador.inventario import Inventario
from itens.ferramentas.Enxada import Enxada
from itens.sementes.SementeDaFloresta import SementeDaFloresta
from itens.ferramentas.Regador import Regador


class Jogador(pygame.sprite.Sprite):

    def __init__(self, pos, group):
        super().__init__(group)
        self.__nome = 'Nome do Principal'      
        self.__inventario = Inventario([3,4])
        self.__z = LAYERS['main']

        # Movimentação
        self.__status = 'baixo' # Refere-se a direção que o player está olhando
        self.__velocidade = 200
        self.__item_atual = None
        self.__em_movimento = False

        # Imports relativos
        self.__dir_atual = os.path.dirname(os.path.abspath(__file__))
        self.__pasta_assets = os.path.join(self.__dir_atual, '..', '..', 'assets', 'ui')
        self.__caminho_imagem = os.path.join(self.__pasta_assets, 'jogador_TESTE.png')
        self.__caminho_sprite = os.path.join(self.__pasta_assets, 'sprite_jogador.png')

        # Carregamento de imagens
        self.__imagem = pygame.image.load(self.__caminho_imagem)
        self.__tabela_sprite = TabelaSprite(pygame.image.load(self.__caminho_sprite))
        self.__animacoes = self.__carrega_animacoes(self.__tabela_sprite)
        self.__direcao_animacao = { 'cima': 3, 'esquerda': 1, 'baixo': 2, 'direita': 0,}
        self.__image = self.__animacoes[self.__direcao_animacao[self.__status]][0]

        # Hitbox
        self.__rect = self.__image.get_rect(midbottom= pos)
        self.__hitbox = pygame.Surface((40,40)).get_rect(midbottom= pos)
        self.__rect = self.__image.get_rect(midbottom= pos)
        
        # Posição
        self.__nova_posicao = pygame.math.Vector2(self.__rect.midbottom)
        self.__posicao = pygame.math.Vector2(self.__rect.midbottom)

        #Adicição de itens provisória
        self.__inventario.adicionar_item(Enxada('Enxada'))
        self.__inventario.adicionar_item(Regador())
        self.__inventario.adicionar_item(SementeDaFloresta(quantidade = 10))
        
        #Comércio
        self.__moedas = 15

    def __carrega_animacoes(self, tabela_sprite: TabelaSprite):
        animacao = []
        animacoes_finais = []
        escala = 2
        for x in range(4):
            animacao.append(tabela_sprite.get_frame(0, x, 64, 64, escala, (0, 0, 0)))
        animacoes_finais.append(animacao)
        
        animacao = []
        for x in range(4):
            animacao.append(tabela_sprite.get_frame(1, x, 64, 64, escala, (0, 0, 0)))
        animacoes_finais.append(animacao)
        escala
        animacao = []
        for x in range(4):
            animacao.append(tabela_sprite.get_frame(2, x, 64, 64, escala, (0, 0, 0)))
        animacoes_finais.append(animacao)
       
        animacao = []
        for x in range(4):
            animacao.append(tabela_sprite.get_frame(3, x, 64, 64, escala, (0, 0, 0)))
        animacoes_finais.append(animacao)
        return animacoes_finais

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
        self.__nova_posicao.x = posicao.x
        self.__nova_posicao.y = posicao.y
        return

    def update(self):
        # Checa se está em movimento
        if self.__posicao[0] != self.__nova_posicao[0] or self.__posicao[1] != self.__nova_posicao[1]:
            self.__em_movimento = True
        else:
            self.__em_movimento = False

        # Atualiza a imagem do jogador
        if self.__em_movimento:
            self.__image = self.__animacoes[self.__direcao_animacao[self.__status]][int(pygame.time.get_ticks() % 400 // 100)]
        else:
            self.__image = self.__animacoes[self.__direcao_animacao[self.__status]][0]
        
        # Atualiza a posicão do jogador
        self.__posicao = self.__nova_posicao.copy()
        self.__rect.midbottom = self.__nova_posicao.copy()
        self.__hitbox.midbottom = self.__nova_posicao.copy()

        if self.__item_atual not in self.__inventario.itens:
            self.__item_atual = None

    def set_inventario(self, inventario):
        self.__inventario = inventario

    @property
    def nome(self):
        return self.__nome

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
        posicao_matriz = [self.__rect.midbottom[0], self.__rect.midbottom[1]]
        for index, posicao in enumerate(posicao_matriz):
            posicao_matriz[index] = int(posicao // 64)
        return posicao_matriz
    
    @property
    def velocidade(self):
        return self.__velocidade
    
    @property
    def imagem(self):
        return self.__imagem
    
    @property
    def item_atual(self):
        return self.__item_atual
    
    @property
    def inventario(self):
        return self.__inventario
    
    @property
    def moedas(self):
        return self.__moedas
    
    def set_moedas(self, moedas):
        self.__moedas = moedas

    @property
    def z(self):
        return self.__z
    
    @property
    def hitbox(self):
        return self.__hitbox