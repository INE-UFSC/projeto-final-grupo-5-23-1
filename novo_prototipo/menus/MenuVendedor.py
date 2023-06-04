import pygame
from menus.ClassesAbstratas.MenuGenerico import MenuGenerico
from entidades.jogador.jogador import Jogador


class MenuVendedor(MenuGenerico):

    def __init__(self, vendedor, caminho_fundo: str):
        super().__init__()
        self.__vendedor = vendedor
        self.__inventario_vendedor = vendedor.inventario
        self.__item_selecionado = 0
        self.__comandos = []
        #Fundo:
        self.__fundo = pygame.image.load(caminho_fundo)
        #Imagem do Vendedor
        self.__imagem_vendedor = vendedor.imagem
        #Imagem de Dialogo
        self.__imagem_dialogo = vendedor.imagem_dialogo
    
    def __calcula_centro(self, window):
        centro_tela = (window.get_width() // 2, window.get_height() // 2) #(x,y)
        return centro_tela

    def checa_eventos(self, eventos):
        for event in eventos:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.notifica_desativa_menu()
                elif event.key == pygame.K_DOWN:
                    if self.__item_selecionado < len(self.__inventario.itens) - 1:
                        self.__item_selecionado += 1
                elif event.key == pygame.K_UP:
                    if self.__item_selecionado > 0:
                        self.__item_selecionado -= 1
                elif event.key == pygame.K_RETURN:
                    #Fazer comando de comprar item
                    #self.__comandos.append(ComandoSelecionaItemAtual(self.__jogador, item))
                    return
                
    def update(self):
        for comando in self.__comandos:
            comando.run()
        self.__comandos.clear()

    def render(self, window):
        centro = self.__calcula_centro(window)

        rect_fundo = self.__fundo.get_rect(center=(centro))
        window.blit(self.__fundo, rect_fundo)

        rect_imagem_vendedor = self.__imagem_vendedor.get_rect(center=(centro[0] - (rect_fundo.width * (195/770)), centro[1] - (rect_fundo.height * (52/570))))
        window.blit(self.__imagem_vendedor, rect_imagem_vendedor)

        rect_imagem_dialogo = self.__imagem_dialogo.get_rect(center=(centro[0] - (rect_fundo.width * (195/770)), centro[1] + (rect_fundo.height * (175/570))))
        window.blit(self.__imagem_dialogo, rect_imagem_dialogo)
    