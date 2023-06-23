import pygame


class BotaoTexto():
    
    def __init__(self, caminho_fundo: str, posicao, selecionado: bool, texto:str, cor_fonte: str = 'white', caminho_fonte: str = 'novo_prototipo/assets/ui/font.ttf', tamanho_fonte:int = 20):
        self.__posicao = posicao
        self.__selecionado = selecionado
        self.__fonte = pygame.font.Font(caminho_fonte, tamanho_fonte)

        #Texto do botão
        self.__texto = self.__fonte.render(texto, True, cor_fonte)
        self.__rect_texto = self.__texto.get_rect()
        #Fundodo do botão
        self.__fundo = pygame.transform.scale(pygame.image.load(caminho_fundo), (self.__rect_texto.width + (self.__rect_texto.width * 0.1), self.__rect_texto.height + (self.__rect_texto.height * 0.8)))
        self.__rect_fundo = self.__fundo.get_rect(center=(self.__posicao))

        self.__rect_texto.center = self.__rect_fundo.center

    @property
    def rect(self):
        return self.__rect_fundo
    
    def render(self, tela):
        tela.blit(self.__fundo, self.__rect_fundo)
        tela.blit(self.__texto, self.__rect_texto)
        if self.__selecionado == True:
            pygame.draw.rect(tela, 'white', pygame.Rect(self.rect.x, self.rect.y, self.rect.width, self.rect.height), 1)