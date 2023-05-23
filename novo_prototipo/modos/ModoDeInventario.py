import pygame

from comandos.ComandoSelecionaItemAtual import ComandoSelecionaItemAtual
from .ClassesAbstratas.ModoGenerico import ModoGenerico

class ModoDeInventario(ModoGenerico):

    def __init__(self, inventario, jogador):
        super().__init__()
        self.__inventario = inventario
        self.__item_selecionado = 0
        self.__comandos = []
        self.__jogador = jogador
        self.titleFont = pygame.font.Font("novo_prototipo/assets/ui/font.ttf", 70)
        self.itemFont = pygame.font.Font("novo_prototipo/assets/ui/font.ttf", 50)

    def checa_eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.notifyQuitRequested()
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.notifyShowGameRequested()
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
            surface = self.itemFont.render(item['title'], True, 'white')
            largura_menu = max(largura_menu, surface.get_width())
            item['surface'] = surface  
        
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
            
            # Cursor
            if index == self.__item_selecionado:
                item['surface'] = self.itemFont.render(item['title'], True, 'cyan')
            else:
                item['surface'] = self.itemFont.render(item['title'], True, 'white')
            
            # Item text
            surface = item['surface']
            window.blit(surface, (largura, altura))

            altura += (200 * surface.get_height()) // 100      




        '''
        posicao_texto = (posicao_inicial[0], posicao_inicial[1] + espacamento_vertical)
        for semente in self.__inventario:
            texto = fonte.render(semente, True, cor_texto)
            window.blit(texto, posicao_texto)
            posicao_texto = (posicao_texto[0], posicao_texto[1] + espacamento_vertical)
        '''
        