import os
import pygame

dir_atual = os.path.dirname(os.path.abspath(__file__))
pasta_assets = os.path.join(dir_atual, '..', '..', 'assets', 'ui')
caminho_botao_pressionado = os.path.join(pasta_assets, 'botao_pressionado.png')
caminho_botao_solto = os.path.join(pasta_assets, 'botao_solto.png')
caminho_fonte = os.path.join(pasta_assets, 'font.ttf')

class BotaoTexto():
    
    def __init__(self, posicao, selecionado: bool, texto:str, cor_fonte: str = 'gray18', caminho_fonte: str = caminho_fonte, tamanho_fonte:int = 20, caminho_fundo_solto: str = caminho_botao_solto, caminho_fundo_pressionado: str = caminho_botao_pressionado):
        self.__posicao = posicao
        self.__selecionado = selecionado
        self.__fonte = pygame.font.Font(caminho_fonte, tamanho_fonte)

        #Texto do botão
        self.__texto = self.__fonte.render(texto, True, cor_fonte)
        self.__rect_texto = self.__texto.get_rect()
        #Fundodo do botão
        self.__fundo_solto = pygame.transform.scale(pygame.image.load(caminho_fundo_solto), (self.__rect_texto.width + (self.__rect_texto.width * 0.2), self.__rect_texto.height + (self.__rect_texto.height * 0.9)))
        self.__fundo_pressionado = pygame.transform.scale(pygame.image.load(caminho_fundo_pressionado), (self.__rect_texto.width + (self.__rect_texto.width * 0.2), self.__rect_texto.height + (self.__rect_texto.height * 0.9)))
        self.__rect_fundo = self.__fundo_solto.get_rect(center=(self.__posicao))

        self.__rect_texto.center = self.__rect_fundo.center

    @property
    def rect(self):
        return self.__rect_fundo
    
    def render(self, tela):
        rect_texto = self.__rect_texto
        if self.__selecionado == False:
            rect_texto.centery -= 5
            rect_texto.centerx += 5
            tela.blit(self.__fundo_solto, self.__rect_fundo)
            tela.blit(self.__texto, rect_texto)
        else:
            rect_texto.centery += 2
            rect_texto.centerx += 5
            tela.blit(self.__fundo_pressionado, self.__rect_fundo)
            tela.blit(self.__texto, rect_texto)