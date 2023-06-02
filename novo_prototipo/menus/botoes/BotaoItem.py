
from itens.Item import Item


class BotaoItem():

    def __init__(self, fundo, posicao, fonte, cor_fonte, item: Item):
        #Informações do botão
        self.__x_pos = posicao[0]
        self.__y_pos = posicao[1]
        self.__fonte = fonte
        self.__cor_fonte = cor_fonte

        #Fundo do botão
        self.__fundo = fundo
        self.__rect_fundo = self.__fundo.get_rect(center=(self.__x_pos, self.__y_pos))

		#Texto do nome do item
        self.__texto_nome = item.nome
        self.__texto_nome_visual = self.__fonte.render(self.__texto_nome, True, self.__cor_fonte)
        self.__texto_nome_visual_rect = self.__texto_nome_visual.get_rect(midleft=self.__calcula_posicao_texto())

        #Texto do preço do item
        self.__texto_preco = item.preco
        self.__texto_preco_visual = self.__fonte.render(self.__texto_preco, True, self.__cor_fonte)
        self.__texto_preco_visual_rect = self.__texto_preco_visual.get_rect(center=self.__calcula_posicao_preco())
        
        #Imagem do item
        self.__imagem_item = item.imagem
        self.__rect_imagem_item = self.__imagem_item.get_rect(center=self.__calcula_posicao_imagem_item())        

    def __calcula_posicao_imagem_item(self):
        posicao_x = self.rect.centerx - (self.rect.width * (1/2))
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
        tela.blit(self.__fundo, self.__rect_fundo)
        tela.blit(self.__imagem_item, self.__rect_imagem_item)
        tela.blit(self.__texto_nome_visual, self.__texto_nome_visual_rect)
        tela.blit(self.__texto_preco_visual, self.__texto_preco_visual_rect)
