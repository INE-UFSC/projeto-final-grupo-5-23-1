import pygame
from menus.ClassesAbstratas.MenuGenerico import MenuGenerico
from entidades.jogador.jogador import Jogador
from menus.botoes.BotaoItem import BotaoItem
from comandos.ComandoComprarItem import ComandoComprarItem


class MenuVendedor(MenuGenerico):

    def __init__(self, jogador, vendedor, caminho_fundo: str):
        super().__init__()
        self.__jogador = jogador
        self.__vendedor = vendedor
        self.__inventario_vendedor = vendedor.inventario
        self.__comandos = []
        #Indices
        self.__item_selecionado = 0
        self.__pagina_atual = 0
        #Fundo 770x570
        self.__fundo = pygame.image.load(caminho_fundo)
        #Imagem do Vendedor 320x310
        self.__imagem_vendedor = vendedor.imagem 
        #Imagem de Dialogo 320x120
        self.__imagem_dialogo = vendedor.imagem_dialogo
        #Texto nome do Vendedor
        self.__fonte_nome_vendedor = pygame.font.Font('novo_prototipo/assets/ui/raidercrusadersemistraight.ttf', 25)
        self.__texto_nome_vendedor = self.__fonte_nome_vendedor.render(vendedor.nome, True, 'white')
        #Botões:
        self.__num_itens_por_pagina = 5
        self.__fonte_botoes = 'novo_prototipo/assets/ui/font.ttf'
        self.__cor_fonte_botoes = 'white'
        self.__botoes = None #Na renderização botoes é inicializado
        
    @property
    def botoes(self):
        return self.__botoes
    
    @botoes.setter
    def botoes(self, botoes):
        self.__botoes = botoes
        return

    def __calcula_centro(self, window):
        centro_tela = (window.get_width() // 2, window.get_height() // 2) #(x,y)
        return centro_tela
    
    def __constroi_matriz_botoes(self, window):
        centro = self.__calcula_centro(window)
        posicoes_botoes = [(centro[0] + 192, centro[1] - 166), (centro[0] + 192, centro[1] - 77), (centro[0] + 192, centro[1] + 14), (centro[0] + 192, centro[1] + 103), (centro[0] + 192, centro[1] + 192)]
        pagina_provisoria = []
        matriz_paginas = []

        indice_botao_provisorio = 0
        for item in self.__inventario_vendedor.itens:
            if indice_botao_provisorio == self.__item_selecionado:
                pagina_provisoria.append(BotaoItem(caminho_fundo='novo_prototipo/assets/ui/fundo_botao_TESTE.png', posicao=posicoes_botoes[indice_botao_provisorio], caminho_fonte=self.__fonte_botoes, cor_fonte=self.__cor_fonte_botoes, item=item, selecionado=True))
            else:
                pagina_provisoria.append(BotaoItem(caminho_fundo='novo_prototipo/assets/ui/fundo_botao_TESTE.png', posicao=posicoes_botoes[indice_botao_provisorio], caminho_fonte=self.__fonte_botoes, cor_fonte=self.__cor_fonte_botoes, item=item, selecionado=False))
            indice_botao_provisorio += 1
            if len(pagina_provisoria) == self.__num_itens_por_pagina:
                matriz_paginas.append(pagina_provisoria)
                pagina_provisoria = []
                indice_botao_provisorio = 0
                
        if len(pagina_provisoria) != 0:
            matriz_paginas.append(pagina_provisoria)

        if matriz_paginas == []:
            self.botoes = [[]]
        else:
            self.botoes = matriz_paginas
        return matriz_paginas

    def checa_eventos(self, eventos):
        for event in eventos:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.notifica_desativa_menu()
                elif event.key == pygame.K_DOWN:
                    if self.__item_selecionado < self.__num_itens_por_pagina -1:
                        self.__item_selecionado += 1
                    elif self.__pagina_atual < len(self.botoes) - 1:
                        self.__item_selecionado = 0
                        self.__pagina_atual += 1
                elif event.key == pygame.K_UP:
                    if self.__item_selecionado > 0:
                        self.__item_selecionado -= 1
                    elif self.__pagina_atual > 0:
                        self.__item_selecionado = 4
                        self.__pagina_atual -= 1
                    
                elif event.key == pygame.K_RETURN:
                    self.__comandos.append(ComandoComprarItem(item=self.__botoes[self.__pagina_atual][self.__item_selecionado].item,jogador=self.__jogador))
                    return
                
    def update(self):
        for comando in self.__comandos:
            comando.run()
        self.__comandos.clear()

    def render(self, window):
        centro = self.__calcula_centro(window)
        self.__constroi_matriz_botoes(window)
        #Fundo
        rect_fundo = self.__fundo.get_rect(center=(centro))
        window.blit(self.__fundo, rect_fundo)
        #Imagem do vendedor
        rect_imagem_vendedor = self.__imagem_vendedor.get_rect(center=(centro[0] - (rect_fundo.width * (195/770)), centro[1] - (rect_fundo.height * (52/570))))
        window.blit(self.__imagem_vendedor, rect_imagem_vendedor)
        #Imagem do dialogo
        rect_imagem_dialogo = self.__imagem_dialogo.get_rect(center=(centro[0] - (rect_fundo.width * (195/770)), centro[1] + (rect_fundo.height * (175/570))))
        window.blit(self.__imagem_dialogo, rect_imagem_dialogo)
        #Nome do vendedor
        rect_texto_nome_vendedor = self.__texto_nome_vendedor.get_rect()
        rect_texto_nome_vendedor.midleft = (rect_imagem_vendedor.midleft[0], rect_imagem_vendedor.centery - (rect_imagem_vendedor.height/2) - (rect_texto_nome_vendedor.height/2))
        window.blit(self.__texto_nome_vendedor, rect_texto_nome_vendedor)
        #Lista de botoes
        for botao in self.botoes[self.__pagina_atual]:
            botao.render(window)