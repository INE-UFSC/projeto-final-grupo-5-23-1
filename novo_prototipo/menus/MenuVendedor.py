import pygame
from menus.ClassesAbstratas.MenuGenerico import MenuGenerico
from entidades.jogador.jogador import Jogador


class MenuVendedor(MenuGenerico):

    def __init__(self, inventario_vendedor, jogador: Jogador):
        super().__init__()
        self.__inventario_vendedor = inventario_vendedor
        self.__jogador = jogador
        self.__item_selecionado = 0
        self.__comandos = []
        
    def checa_eventos(self, eventos):
        for event in eventos:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_i:
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

    