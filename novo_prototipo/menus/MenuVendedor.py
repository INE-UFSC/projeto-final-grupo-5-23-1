from itens.Item import Item
import pygame
from menus.ClassesAbstratas.MenuGenerico import MenuGenerico
from entidades.jogador.jogador import Jogador
from menus.botoes.BotaoItem import BotaoItem
from comandos.ComandoComprarItem import ComandoComprarItem
from comandos.ComandoVenderItem import ComandoVenderItem
from comandos.ComandoFechaMenu import ComandoFechaMenu


class MenuVendedor(MenuGenerico):

    def __init__(self, jogador: Jogador, vendedor, caminho_fundo: str, caminho_seta: str):
        super().__init__()
        self.__jogador = jogador
        self.__vendedor = vendedor
        self.__inventario_selecionado = {'Comprar' : vendedor.inventario, "Vender" : self.__jogador.inventario}
        self.__comandos = []
        self.__lista_botoes_vazia = False
        #Indices
        self.__item_selecionado = 0
        self.__pagina_atual_inventario = 0
        self.__modo_vendedor = 'Comprar'
        #Fundo 770x570
        self.__fundo = pygame.image.load(caminho_fundo)
        #Coluna da esquerda:
        #Imagem do Vendedor 320x310
        self.__imagem_vendedor = vendedor.imagem 
        #Imagem de Dialogo 320x120
        self.__imagem_dialogo = vendedor.imagem_dialogo
        #Texto nome do Vendedor
        self.__fonte_nome_vendedor = pygame.font.Font('novo_prototipo/assets/ui/raidercrusadersemistraight.ttf', 25)
        self.__texto_nome_vendedor = self.__fonte_nome_vendedor.render(vendedor.nome, True, 'white')
        
        
        #Coluna da direita:
        #Texto 'Comprar':
        self.__fonte_comprar = pygame.font.Font('novo_prototipo/assets/ui/font.ttf', 16)
        self.__texto_comprar = self.__fonte_comprar.render('Comprar', True, 'White')
        #Texto 'Vender':
        self.__fonte_vender = pygame.font.Font('novo_prototipo/assets/ui/font.ttf', 16)
        self.__texto_vender = self.__fonte_vender.render('Vender', True, 'White')
        #Imagem moeda do jogo: 25x25
        self.__imagem_moeda = pygame.image.load('novo_prototipo/assets/ui/imagem_moeda_TESTE.png')
        #Número de moedas do jogador
        self.__fonte_texto_numero_moedas = pygame.font.Font('novo_prototipo/assets/ui/font.ttf', 16)
        self.__texto_numero_moedas = self.__fonte_texto_numero_moedas.render(str(self.__jogador.moedas), True, 'White')
        #Botões: 320x82
        self.__num_itens_por_pagina = 5
        self.__fonte_botoes = 'novo_prototipo/assets/ui/font.ttf'
        self.__cor_fonte_botoes = 'white'
        self.__botoes = None #Na renderização botoes é inicializado
        #Seta abaixo da lista de botões: 61x21
        self.__imagem_seta = pygame.image.load(caminho_seta)

    @property
    def botoes(self):
        return self.__botoes
    
    @botoes.setter
    def botoes(self, botoes):
        self.__botoes = botoes
        return
    
    @property
    def lista_botoes_vazia(self):
        return self.__lista_botoes_vazia
    
    @lista_botoes_vazia.setter
    def lista_botoes_vazia(self, lista_botoes_vazia: bool):
        if isinstance(lista_botoes_vazia, bool):
            self.__lista_botoes_vazia = lista_botoes_vazia

    def __calcula_centro(self, window):
        centro_tela = (window.get_width() // 2, window.get_height() // 2) #(x,y)
        return centro_tela
    
    def __constroi_matriz_botoes(self, window):
        centro = self.__calcula_centro(window)
        posicoes_botoes = [(centro[0] + 192, centro[1] - 166), (centro[0] + 192, centro[1] - 77), (centro[0] + 192, centro[1] + 14), (centro[0] + 192, centro[1] + 103), (centro[0] + 192, centro[1] + 192)]
        pagina_provisoria = []
        matriz_paginas = []
        itens = self.__inventario_selecionado[self.__modo_vendedor].itens

        indice_botao_provisorio = 0
        for item in itens:
            if isinstance(item, Item):
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
                    self.__comandos.append(ComandoFechaMenu(self))

                elif event.key == pygame.K_DOWN:
                    
                    if self.__item_selecionado < len(self.__botoes[self.__pagina_atual_inventario]) -1:
                        self.__item_selecionado += 1
                    elif self.__pagina_atual_inventario < len(self.botoes) - 1:
                        self.__item_selecionado = 0
                        self.__pagina_atual_inventario += 1

                elif event.key == pygame.K_UP:
                    if self.__item_selecionado > 0:
                        self.__item_selecionado -= 1
                    elif self.__pagina_atual_inventario > 0:
                        self.__item_selecionado = 4
                        self.__pagina_atual_inventario -= 1
                
                elif event.key == pygame.K_RIGHT:
                    self.__pagina_atual_inventario = 0
                    self.__modo_vendedor = 'Vender'

                elif event.key == pygame.K_LEFT:
                    self.__pagina_atual_inventario = 0
                    self.__modo_vendedor = 'Comprar'
                    
                elif event.key == pygame.K_RETURN:
                    if self.lista_botoes_vazia == False:
                        if self.__modo_vendedor == 'Comprar':
                            self.__comandos.append(ComandoComprarItem(item=self.__botoes[self.__pagina_atual_inventario][self.__item_selecionado].item,jogador=self.__jogador))
                        elif self.__modo_vendedor == 'Vender':
                            self.__comandos.append(ComandoVenderItem(item=self.__botoes[self.__pagina_atual_inventario][self.__item_selecionado].item,jogador=self.__jogador))
                    return
                
    def update(self):
        for comando in self.__comandos:
            comando.run()
        self.__comandos.clear()

        if self.__inventario_selecionado[self.__modo_vendedor].capacidade_atual == 0:
            self.lista_botoes_vazia = True
        else:
            self.lista_botoes_vazia = False
        while True:
            if (self.__item_selecionado > 0) and (self.__item_selecionado > len(self.botoes[self.__pagina_atual_inventario]) - 1):
                self.__item_selecionado -= 1
            else:
                break
        
        self.__texto_numero_moedas = self.__fonte_texto_numero_moedas.render(str(self.__jogador.moedas), True, 'White')

    def render(self, window):
        centro = self.__calcula_centro(window)
        self.__constroi_matriz_botoes(window)

        #Coluna da esquerda:
        
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

        
        #Coluna da direita:
        if self.__modo_vendedor == 'Comprar':
            #Texto 'Comprar':
            self.__texto_comprar = self.__fonte_comprar.render('Comprar', True, 'White')
            rect_texto_comprar = self.__texto_comprar.get_rect()
            rect_texto_comprar.midleft = (centro[0] + 33, centro[1] - 225)
            window.blit(self.__texto_comprar, rect_texto_comprar)

            #Texto 'Vender':
            self.__texto_vender = self.__fonte_vender.render('Vender', True, 'azure4')
            rect_texto_vender = self.__texto_vender.get_rect()
            rect_texto_vender.midleft = (rect_texto_comprar.midright[0] + 15, centro[1] - 225)
            window.blit(self.__texto_vender, rect_texto_vender)

        elif self.__modo_vendedor == 'Vender':
            #Texto 'Comprar':
            self.__texto_comprar = self.__fonte_comprar.render('Comprar', True, 'azure4')
            rect_texto_comprar = self.__texto_comprar.get_rect()
            rect_texto_comprar.midleft = (centro[0] + 33, centro[1] - 225)
            window.blit(self.__texto_comprar, rect_texto_comprar)

            #Texto 'Vender':
            self.__texto_vender = self.__fonte_vender.render('Vender', True, 'White')
            rect_texto_vender = self.__texto_vender.get_rect()
            rect_texto_vender.midleft = (rect_texto_comprar.midright[0] + 15, centro[1] - 225)
            window.blit(self.__texto_vender, rect_texto_vender)

        #Quantidade de moedas jogador:
        rect_texto_numero_moedas = self.__texto_numero_moedas.get_rect(midright=(centro[0] + 346, centro[1] - 225))
        window.blit(self.__texto_numero_moedas, rect_texto_numero_moedas)
        rect_imagem_moeda = self.__imagem_moeda.get_rect(midright=(rect_texto_numero_moedas.midleft[0] - 10, rect_texto_numero_moedas.midleft[1]))
        window.blit(self.__imagem_moeda, rect_imagem_moeda)

        #Lista de botoes
        for botao in self.botoes[self.__pagina_atual_inventario]:
            botao.render(window)

        #Seta
        if len(self.botoes[self.__pagina_atual_inventario]) == 5:
            rect_seta = self.__imagem_seta.get_rect(center=(self.botoes[self.__pagina_atual_inventario][4].rect.centerx, self.botoes[self.__pagina_atual_inventario][4].rect.centery + 59))
            window.blit(self.__imagem_seta, rect_seta)