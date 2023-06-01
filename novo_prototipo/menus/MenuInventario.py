import pygame

from comandos.ComandoSelecionaItemAtual import ComandoSelecionaItemAtual
from itens.ItemQuantizavel import ItemQuantizavel
from menus.ClassesAbstratas.MenuGenerico import MenuGenerico

class MenuInventario(MenuGenerico):

    def __init__(self, inventario, jogador):
        super().__init__()
        self.__inventario = inventario
        self.__item_selecionado = 0
        self.__comandos = []
        self.__jogador = jogador
        self.titleFont = pygame.font.Font("novo_prototipo/assets/ui/font.ttf", 70)
        self.itemFont = pygame.font.Font("novo_prototipo/assets/ui/font.ttf", 50)

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
                    item = self.__inventario.itens[self.__item_selecionado]
                    self.__comandos.append(ComandoSelecionaItemAtual(self.__jogador, item))
    
    def update(self):
        for comando in self.__comandos:
            comando.run()
        self.__comandos.clear()

    def render(self, window):
        largura_menu = 0
        for item in self.__inventario.itens:
            surface = self.itemFont.render(item.nome, True, 'white')
            largura_menu = max(largura_menu, surface.get_width())

        # Altura inicial
        altura = 100
        
        # Titulo
        surface = self.titleFont.render("Inventário", True, 'white')
        largura = (window.get_width() - surface.get_width()) // 2
        window.blit(surface, (largura, altura))
        altura += (250 * surface.get_height()) // 100
        
        # Desenha o inventario
        largura = (window.get_width() - largura_menu) // 2
        for index, item in enumerate(self.__inventario.itens):
            if isinstance(item, ItemQuantizavel):
                string_de_representação = item.nome + f'     x{item.quantidade}'
            else:
                string_de_representação = item.nome
            # Cursor
            if index == self.__item_selecionado:
                surface = self.itemFont.render(string_de_representação, True, 'cyan')
            else:
                surface = self.itemFont.render(string_de_representação, True, 'white')
            
            # Item text
            window.blit(surface, (largura, altura))

            altura += (200 * surface.get_height()) // 100      
