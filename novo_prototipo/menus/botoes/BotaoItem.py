
import pygame
from itens.Item import Item
import os

dir_atual = os.path.dirname(os.path.abspath(__file__))
pasta_assets = os.path.join(dir_atual, '..', '..', 'assets', 'ui')
caminho_fundo = os.path.join(pasta_assets, 'fundo_botao.png')
caminho_fundo_selecionado = os.path.join(pasta_assets, 'fundo_botao_selecionado.png')

class BotaoItem():

    def __init__(self, posicao, caminho_fonte: str, cor_fonte, item: Item, selecionado: bool, caminho_fundo: str = caminho_fundo):
        #Informações do botão
        self.__x_pos = posicao[0]
        self.__y_pos = posicao[1]
        self.__caminho_fonte = caminho_fonte
        self.__fonte = pygame.font.Font(self.__caminho_fonte, 15)
        self.__cor_fonte = cor_fonte
        self.__item = item

        #Fundo do botão 320x82
        self.__fundo = pygame.image.load(caminho_fundo)
        self.__fundo_selecionado = pygame.image.load(caminho_fundo_selecionado)
        self.__rect_fundo = self.__fundo.get_rect(center=(self.__x_pos, self.__y_pos))

		#Texto do nome do item
        self.__texto_nome = item.nome
        self.__texto_nome_visual = self.__fonte.render(self.__texto_nome, True, self.__cor_fonte)
        self.__texto_nome_visual_rect = self.__texto_nome_visual.get_rect(midleft=self.__calcula_posicao_texto())

        #Texto do preço do item
        self.__texto_preco = str(item.preco)
        self.__texto_preco_visual = self.__fonte.render(self.__texto_preco, True, self.__cor_fonte)
        self.__texto_preco_visual_rect = self.__texto_preco_visual.get_rect(center=self.__calcula_posicao_preco())
        
        #Imagem do item
        self.__imagem_item = pygame.transform.scale(item.imagem, (72, 72))
        self.__rect_imagem_item = self.__imagem_item.get_rect(center=self.__calcula_posicao_imagem_item())        
        
        #Seleção
        self.__selecionado = selecionado

    @property
    def rect(self):
        return self.__rect_fundo
    
    @property
    def item(self):
        return self.__item

    #Métodos internos para calcular a posição dos componentes do botão:    
    def __calcula_posicao_imagem_item(self):
        posicao_x = self.rect.centerx - (self.rect.width * (119/320))
        posicao_y = self.rect.centery
        return (posicao_x, posicao_y)
    
    def __calcula_posicao_texto(self):
        posicao_x = self.rect.centerx - (self.rect.width * (9/40))
        posicao_y = self.rect.centery
        return (posicao_x, posicao_y)
    
    def __calcula_posicao_preco(self):
        posicao_x = self.rect.centerx + (self.rect.width * (2/5))
        posicao_y = self.rect.centery
        return (posicao_x, posicao_y)

    def render(self, tela):
        if self.__selecionado == False:
            tela.blit(self.__fundo, self.__rect_fundo)
        else:
            tela.blit(self.__fundo_selecionado, self.__rect_fundo)
        tela.blit(self.__imagem_item, self.__rect_imagem_item)
        tela.blit(self.__texto_nome_visual, self.__texto_nome_visual_rect)
        tela.blit(self.__texto_preco_visual, self.__texto_preco_visual_rect)