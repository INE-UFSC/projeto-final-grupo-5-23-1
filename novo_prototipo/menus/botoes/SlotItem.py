import pygame
from itens.Item import Item
from itens.ItemQuantizavel import ItemQuantizavel


class SlotItem():

    def __init__(self, posicao, selecionado: bool, item: Item = None, caminho_fundo: str = 'novo_prototipo/assets/ui/fundo_slot_TESTE.png', caminho_fonte: str = 'novo_prototipo/assets/ui/font.ttf', cor_fonte: str = 'White'):
        self.__x_pos = posicao[0]
        self.__y_pos = posicao[1]
        self.__caminho_fonte = caminho_fonte
        self.__fonte = pygame.font.Font(self.__caminho_fonte, 15)
        self.__cor_fonte = cor_fonte
        self.__item = item

        #Fundo do botão
        self.__fundo = pygame.image.load(caminho_fundo)
        self.__rect_fundo = self.__fundo.get_rect(topleft=(self.__x_pos, self.__y_pos))

        #Imagem do item
        if self.__item != None:
            self.__imagem_item = pygame.transform.scale(item.imagem, (self.rect.width - 6, self.rect.height - 6))
            self.__rect_imagem_item = self.__imagem_item.get_rect(center=self.rect.center)

        #Texto da quantidade do item
        if isinstance(self.__item, ItemQuantizavel):
            self.__texto_quantidade = str(item.quantidade)
            self.__texto_quantidade_visual = self.__fonte.render(self.__texto_quantidade, True, self.__cor_fonte)
            self.__texto_quantidade_visual_rect = self.__texto_quantidade_visual.get_rect(center=self.__calcula_posicao_quantidade())

        #Seleção
        self.__selecionado = selecionado

    @property
    def item(self):
        return self.__item
    
    @item.setter
    def item(self, item):
        self.__item = item
    
    @property
    def rect(self):
        return self.__rect_fundo
    
    def __calcula_posicao_quantidade(self):
        posicao_x = self.rect.centerx + (self.rect.width * (17/72))
        posicao_y = self.rect.centery + (self.rect.height * (19/72))
        return (posicao_x, posicao_y)
    
    def adiciona_item(self, item_a_ser_adicionado):
        if isinstance(item_a_ser_adicionado, Item):
            if self.item == None:
                classe_item = item_a_ser_adicionado.__class__
                novo_item = classe_item()
                self.item = novo_item
            elif isinstance(item_a_ser_adicionado, ItemQuantizavel):
                if item_a_ser_adicionado.nome == self.item.nome:
                    self.item.aumenta_quantidade(item_a_ser_adicionado.quantidade)

    def remove_item(self):
        self.item = None                    
    
    def render(self, tela):
        tela.blit(self.__fundo, self.__rect_fundo)
        if self.__item != None:
            tela.blit(self.__imagem_item, self.__rect_imagem_item)
            if isinstance(self.__item, ItemQuantizavel):
                tela.blit(self.__texto_quantidade_visual, self.__texto_quantidade_visual_rect)
        if self.__selecionado == True:
            pygame.draw.rect(tela, 'crimson', pygame.Rect(self.rect.x, self.rect.y, self.rect.width, self.rect.height), 1)
