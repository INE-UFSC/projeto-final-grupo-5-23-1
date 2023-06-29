import pygame
from menus.ClassesAbstratas.MenuGenerico import MenuGenerico
from menus.botoes.BotaoTexto import BotaoTexto
from comandos.ComandoDesbloquearBarreira import ComandoDesbloquearBarreira
from comandos.ComandoFechaMenu import ComandoFechaMenu
import os

dir_atual = os.path.dirname(os.path.abspath(__file__))
pasta_assets = os.path.join(dir_atual, '..', 'assets', 'ui')
caminho_fundo = os.path.join(pasta_assets, 'fundo_menu_desbloqueio.png')
caminho_fonte = os.path.join(pasta_assets, 'font.ttf')

class MenuDesbloqueio(MenuGenerico):
    
    def __init__(self, barreira,jogador):
        super().__init__()
        self.__barreira = barreira
        self.__jogador = jogador
        self.__comandos = []

        # Fonte
        self.__fonte = pygame.font.Font(caminho_fonte, 20)

        #  Informações para centralizar menu
        self.__tamanho_tela = list(pygame.display.get_window_size())
        self.__centro_tela = (self.__tamanho_tela[0] / 2, self.__tamanho_tela[1] / 2)

        # Fundo do menu
        self.__fundo = pygame.image.load(caminho_fundo)
        self.__rect_fundo = self.__fundo.get_rect(center=(self.__centro_tela))

        # Botoes
        self.__indice_selecionado = 0
        self.__lista_botoes = self.__criar_botoes()

        # Texto do menu
        self.__texto_0 = self.__fonte.render('Você deseja desblo-', True, 'white')
        self.__rect_texto_0 = self.__texto_0.get_rect(center=(self.__centro_tela[0], self.__centro_tela[1]-35))
        self.__texto_1 = self.__fonte.render('quear a próxima cúpula', True, 'white')
        self.__rect_texto_1 = self.__texto_1.get_rect(center=(self.__centro_tela[0], self.__centro_tela[1]-10))
        self.__texto_2 = self.__fonte.render(f'por {barreira.custo}?', True, 'white')
        self.__rect_texto_2 = self.__texto_2.get_rect(center=(self.__centro_tela[0], self.__centro_tela[1]+15))

    def __criar_botoes(self):
        lista_botoes = []
        posicao_botao_desbloqueio = (self.__rect_fundo.centerx - 110, self.__rect_fundo.centery + 75)
        if self.__indice_selecionado == 0:
            botao_desbloqueio = BotaoTexto(posicao=posicao_botao_desbloqueio,selecionado=True,texto='Desbloquear')
        else:
            botao_desbloqueio = BotaoTexto(posicao=posicao_botao_desbloqueio,selecionado=False,texto='Desbloquear')
        posicao_botao_cancelar = (botao_desbloqueio.rect.midright[0] + 120, botao_desbloqueio.rect.midright[1])
        if self.__indice_selecionado == 1:
            botao_cancelar = BotaoTexto(posicao=posicao_botao_cancelar,selecionado=True,texto='Cancelar')
        else:
            botao_cancelar = BotaoTexto(posicao=posicao_botao_cancelar,selecionado=False,texto='Cancelar')
        lista_botoes.append(botao_desbloqueio)
        lista_botoes.append(botao_cancelar)
        return lista_botoes

    def checa_eventos(self, eventos):
        for event in eventos:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_i:
                    self.notifica_desativa_menu()
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    novo_indice = self.__indice_selecionado - 1
                    if novo_indice < 0:
                        novo_indice = len(self.__lista_botoes) - 1
                    self.__indice_selecionado = novo_indice
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    novo_indice = self.__indice_selecionado + 1
                    if novo_indice > len(self.__lista_botoes) - 1:
                        novo_indice = 0
                    self.__indice_selecionado = novo_indice
                elif event.key == pygame.K_RETURN or event.key == pygame.K_e:
                    if self.__indice_selecionado == 0:
                        moedas_resultante = self.__jogador.moedas - self.__barreira.custo
                        if moedas_resultante >= 0:
                            self.__comandos.append(ComandoDesbloquearBarreira(self.__jogador, self.__barreira))
                            self.__comandos.append(ComandoFechaMenu(self))
                    elif self.__indice_selecionado == 1:
                        self.__comandos.append(ComandoFechaMenu(self))
                        
    def update(self):
        for comando in self.__comandos:
            comando.run()
        self.__comandos.clear()
        self.__lista_botoes = self.__criar_botoes()

    def render(self, tela):
        #Fundo
        tela.blit(self.__fundo, self.__rect_fundo)

        for botao in self.__lista_botoes:
            botao.render(tela)

        tela.blit(self.__texto_0, self.__rect_texto_0)
        tela.blit(self.__texto_1, self.__rect_texto_1)
        tela.blit(self.__texto_2, self.__rect_texto_2)