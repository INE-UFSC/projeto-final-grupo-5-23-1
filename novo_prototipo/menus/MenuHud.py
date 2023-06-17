import pygame
from menus.ClassesAbstratas.MenuGenerico import MenuGenerico
from menus.botoes.SlotItem import SlotItem
from comandos.ComandoSelecionaItemAtual import ComandoSelecionaItemAtual


class MenuHud(MenuGenerico):

    def __init__(self, inventario, jogador):
        super().__init__()
        self.__inventario = inventario.itens[0:inventario.tamanho_matriz[0]]
        self.__jogador = jogador
        self.__indice_selecionado = 0
        self.__comandos = []

        
        #Informações para a matriz do inventário
        self.__numero_slots = inventario.tamanho_matriz[0]
        self.__espacamento_slots = 10
        self.__slots_hud = self.__criar_slots()

    def __atualiza_itens(self, jogador):
        self.__inventario = jogador.inventario.itens[0:3]
        self.__jogador = jogador
        self.__slots_hud = self.__criar_slots()
        return
    
    def __calcula_posicao_inicial(self):
        tamanho_tela = list(pygame.display.get_window_size())
        posicao_inicial = (tamanho_tela[0] * (28/768), tamanho_tela[1] - (tamanho_tela[1] * (106 / 768)))
        return posicao_inicial

    def __criar_slots(self):
        posicao_inicial = self.__calcula_posicao_inicial() #Inicia em um valor e depois é incrementado nos próximos slots
        
        slots_hud = []

        posicao = list(posicao_inicial)
        
        for i in range(self.__numero_slots):
            
            item = self.__inventario[i]
            
            #Seleção visual de slots
            if self.__indice_selecionado == i:
                slot = SlotItem(selecionado=True,item=item,posicao=posicao)
            else:
                slot = SlotItem(selecionado=False,item=item,posicao=posicao)

            slots_hud.append(slot)
            #Espaçamento horizontal entre slots
            posicao[0] += slot.rect.width + self.__espacamento_slots

        return slots_hud
    
    def checa_eventos(self, eventos):
        for event in eventos:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    self.__indice_selecionado = 0
                elif event.key == pygame.K_2:
                    self.__indice_selecionado = 1
                elif event.key == pygame.K_3:
                    self.__indice_selecionado = 2
                self.__comandos.append(ComandoSelecionaItemAtual(self.__jogador, self.__inventario[self.__indice_selecionado]))
        
                        
    def update(self, jogador):
        for comando in self.__comandos:
            comando.run()
        self.__comandos.clear()
        self.__atualiza_itens(jogador)

    def render(self, tela):
        for slot in self.__slots_hud:
            slot.render(tela)