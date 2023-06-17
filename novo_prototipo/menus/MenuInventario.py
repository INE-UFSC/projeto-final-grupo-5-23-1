import pygame

from comandos.ComandoSelecionaItemAtual import ComandoSelecionaItemAtual
from menus.ClassesAbstratas.MenuGenerico import MenuGenerico
from .botoes.SlotItem import SlotItem

class MenuInventario(MenuGenerico):

    def __init__(self, inventario, jogador):
        super().__init__()
        self.__inventario = inventario
        self.__jogador = jogador
        self.__indice_selecionado = [0, 0]
        self.__item_selecionado = None
        self.__indice_item_selecionado = None
        self.__comandos = []
        
        #Informações para centralizar menu
        self.__tamanho_tela = list(pygame.display.get_window_size())
        self.__centro_tela = (self.__tamanho_tela[0] / 2, self.__tamanho_tela[1] / 2)

        #Fundo do menu
        self.__fundo = pygame.image.load('novo_prototipo/assets/ui/fundo_menu_TESTE.png')
        self.__rect_fundo = self.__fundo.get_rect(center=(self.__centro_tela))
        #Imagem jogador
        self.__imagem_jogador = self.__jogador.imagem
        self.__rect_imagem_jogador = self.__imagem_jogador.get_rect(center=(self.__centro_tela[0] - (self.__rect_fundo.width * (195/770)), self.__centro_tela[1] - (self.__rect_fundo.height * (52/570))))
        #Texto nome do jogador
        self.__fonte_nome_jogador = pygame.font.Font('novo_prototipo/assets/ui/raidercrusadersemistraight.ttf', 25)
        self.__texto_nome_jogador = self.__fonte_nome_jogador.render(jogador.nome, True, 'white')
        self.__rect_texto_nome_jogador = self.__texto_nome_jogador.get_rect()
        self.__rect_texto_nome_jogador.midleft = (self.__rect_imagem_jogador.midleft[0], self.__rect_imagem_jogador.centery - (self.__rect_imagem_jogador.height/2) - (self.__rect_texto_nome_jogador.height/2))
        #Fundo Status
        self.__fundo_status = pygame.image.load('novo_prototipo/assets/ui/fundo_status_TESTE.png')        
        self.__rect_fundo_status = self.__fundo_status.get_rect(center=(self.__centro_tela[0] - (self.__rect_fundo.width * (195/770)), self.__centro_tela[1] + (self.__rect_fundo.height * (175/570))))
        #Informações para a matriz do inventário
        self.__nro_colunas = self.__inventario.tamanho_matriz[0]
        self.__nro_linhas = self.__inventario.tamanho_matriz[1]
        self.__espacamento_slots = 4
        self.__tamanho_slots = 78
        self.__inventario_matriz = self.__criar_matriz()
        
        #Fonte
        self.itemFont = pygame.font.Font("novo_prototipo/assets/ui/font.ttf", 50)
    
    def __calcula_centro_matriz(self):
        posicao_x = self.__centro_tela[0] + (self.__rect_fundo.width * (189/770)) - ((self.__nro_colunas * self.__tamanho_slots) + (self.__nro_colunas - 1) * self.__espacamento_slots)/2
        posicao_y = self.__centro_tela[1] - ((self.__nro_linhas * self.__tamanho_slots) + (self.__nro_colunas - 1) * self.__espacamento_slots)/2
        return(posicao_x, posicao_y)
    
    def __criar_matriz(self):
        
        posicao_inicial = self.__calcula_centro_matriz() #Inicia em um valor e depois é incrementado nos próximos slots
        
        inventario_matriz = []

        posicao = list(posicao_inicial)
        indice_atual = 0
        for linha in range(self.__nro_linhas):
            linha_atual = []
            for coluna in range(self.__nro_colunas):
                #Verifica a existencia de um item para aquele slot
                try:
                    item = self.__inventario.itens[indice_atual]
                except IndexError:
                    item = None
                
                #Seleção visual de slots
                if self.__indice_selecionado == [linha, coluna]:
                    slot = SlotItem(selecionado=True,item=item,posicao=posicao)
                else:
                    slot = SlotItem(selecionado=False,item=item,posicao=posicao)

                linha_atual.append(slot)
                #Espaçamento horizontal entre slots
                posicao[0] += slot.rect.width + self.__espacamento_slots
                indice_atual += 1
            inventario_matriz.append(linha_atual)
            #Espaçamento vertical entre slots
            posicao[1] += slot.rect.height + self.__espacamento_slots
            posicao[0] = posicao_inicial[0]

        return inventario_matriz

    def checa_eventos(self, eventos):
        for event in eventos:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_i:
                    self.notifica_desativa_menu()
                elif event.key == pygame.K_DOWN:
                    if self.__indice_selecionado[0] < self.__nro_linhas - 1:
                        self.__indice_selecionado[0] += 1
                elif event.key == pygame.K_UP:
                    if self.__indice_selecionado[0] > 0:
                        self.__indice_selecionado[0] -= 1
                elif event.key == pygame.K_LEFT:
                    if self.__indice_selecionado[1] > 0:
                        self.__indice_selecionado[1] -= 1
                elif event.key == pygame.K_RIGHT:
                    if self.__indice_selecionado[1] < self.__nro_colunas - 1:
                        self.__indice_selecionado[1] += 1
                elif event.key == pygame.K_RETURN:
                    if self.__item_selecionado == None:
                        item = self.__inventario_matriz[self.__indice_selecionado[0]][self.__indice_selecionado[1]].item
                        self.__indice_item_selecionado = self.__indice_selecionado[1] + self.__indice_selecionado[0] * (self.__inventario.tamanho_matriz[1] - 1)
                        self.__item_selecionado = item
                    else:
                        indice_substituido = self.__indice_selecionado[1] + self.__indice_selecionado[0] *(self.__inventario.tamanho_matriz[1] - 1)
                        self.__jogador.inventario.itens[self.__indice_item_selecionado] = self.__jogador.inventario.itens[indice_substituido]
                        self.__jogador.inventario.itens[indice_substituido] = self.__item_selecionado
                        self.__item_selecionado = None
                        self.__indice_item_selecionado = None
    def update(self):
        for comando in self.__comandos:
            comando.run()
        self.__comandos.clear()

        self.__inventario_matriz = self.__criar_matriz()

    def render(self, window):
        #Fundo
        window.blit(self.__fundo, self.__rect_fundo)
        
        #Coluna da esquerda:

        #Imagem do jogador
        window.blit(self.__imagem_jogador, self.__rect_imagem_jogador)
        #Fundo status
        window.blit(self.__fundo_status, self.__rect_fundo_status)
        #Nome do jogador
        window.blit(self.__texto_nome_jogador, self.__rect_texto_nome_jogador)

        #Coluna da direita:

        #Matriz de itens
        for linha in self.__inventario_matriz:
            for slot in linha:
                slot.render(window)

