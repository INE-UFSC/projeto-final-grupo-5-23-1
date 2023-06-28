import os
from .ClassesAbstratas.ModoGenerico import ModoGenerico

import pygame
'''
Esta classe implementa o modo de jogo Menu, o qual tem os métodos
"checa_eventos", "update", "render";
'''
class ModoMenuPrincipal(ModoGenerico):
    def __init__(self):        
        super().__init__()
        self.__opcoes_audio_ativa = False
        self.__instrucoes_ativa = False
        #Informações para centralizar menu
        self.__tamanho_tela = list(pygame.display.get_window_size())
        self.__centro_tela = (self.__tamanho_tela[0] / 2, self.__tamanho_tela[1] / 2)

        self.__dir_atual = os.path.dirname(os.path.abspath(__file__))
        self.__pasta_assets = os.path.join(self.__dir_atual, '..', 'assets', 'ui')
        self.__caminho_fundo = os.path.join(self.__pasta_assets, 'fundo_menu_principal.png')
        self.__caminho_fonte = os.path.join(self.__pasta_assets, 'font.ttf')
        self.__caminho_tela_instrucao = os.path.join(self.__pasta_assets, 'tela_instrucao.png')

        # Font
        self.titleFont = pygame.font.Font(self.__caminho_fonte, 60)
        self.itemFont = pygame.font.Font(self.__caminho_fonte, 80)

        # Tela de instruções
        self.__tela_instrucao = pygame.transform.scale(pygame.image.load(self.__caminho_tela_instrucao), (1280, 768))

        # Fundo
        self.__fundo = pygame.transform.scale(pygame.image.load(self.__caminho_fundo), (1280, 768))
        self.__rect_fundo = self.__fundo.get_rect(center=self.__centro_tela)
        
        # Menu principal items
        self.menuPrincipalItems = [
            {
                'title': 'Jogar',
                'action': lambda: self.notifica_desativa_menu_principal()
            },
            {
                'title': 'Instruções',
                'action': lambda: self.mostra_instrucoes()
            },
            {
                'title': 'Audio',
                'action': lambda: self.mostra_opcoes_audio()
            },
            {
                'title': 'Quit',
                'action': lambda: self.notifyQuitRequested()
            }
        ]

        # Menu audio items
        self.menuAudioItems = [
            {
                'title': 'Volume',
                'action1': lambda: self.notifica_aumenta_volume(),
                'action2': lambda: self.notifica_baixa_volume()
            },
            {
                'title': 'Voltar',
                'action': lambda: self.oculta_opcoes_audio()
            }
        ]

        # Menu Items atual
        self.__menuItemsAtual = self.menuPrincipalItems


        # Compute menu width
        self.menuWidth = 0
        self.atualiza_largura_menu()
        
        self.currentMenuItem = 0

    def atualiza_largura_menu(self):
        largura_menu = 0
        for item in self.__menuItemsAtual:
            surface = self.itemFont.render(item['title'], True, 'white')
            largura_menu = max(largura_menu, surface.get_width())
            item['surface'] = surface  
        self.menuWidth = largura_menu

    def mostra_opcoes_audio(self):
        self.__opcoes_audio_ativa = True  

    def oculta_opcoes_audio(self):
        self.__opcoes_audio_ativa = False
    
    def mostra_instrucoes(self):
        self.__instrucoes_ativa = True
    
    def oculta_instrucoes(self):
        self.__instrucoes_ativa = False

    def checa_eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.notifyQuitRequested()
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if self.currentMenuItem < len(self.__menuItemsAtual) - 1:
                        self.currentMenuItem += 1
                elif event.key == pygame.K_UP:
                    if self.currentMenuItem > 0:
                        self.currentMenuItem -= 1
                if event.key == pygame.K_RETURN or event.key == pygame.K_e:
                    if not self.__instrucoes_ativa:
                        menuItem = self.__menuItemsAtual[self.currentMenuItem]
                        try:
                            if self.currentMenuItem != 0 or not self.__opcoes_audio_ativa:
                                menuItem['action']()
                        except Exception as ex:
                            print(ex)
                    else:
                        self.oculta_instrucoes()
                    self.currentMenuItem = 0

                if self.currentMenuItem == 0 and self.__opcoes_audio_ativa:
                    if event.key == pygame.K_RIGHT:
                        menuItem = self.__menuItemsAtual[self.currentMenuItem]
                        menuItem['action1']()
                    elif event.key == pygame.K_LEFT:
                        menuItem = self.__menuItemsAtual[self.currentMenuItem]
                        menuItem['action2']()

                        
    def update(self):
        self.menuAudioItems = [
            {
                'title': f'Volume {round(pygame.mixer.music.get_volume()*10)}',
                'action1': lambda: self.notifica_aumenta_volume(),
                'action2': lambda: self.notifica_baixa_volume()
            },
            {
                'title': 'Voltar',
                'action': lambda: self.oculta_opcoes_audio()
            }
        ]
        self.atualiza_largura_menu()
        
    def render(self, window):
        
        if not self.__instrucoes_ativa:
            # Fundo:
            window.blit(self.__fundo, self.__rect_fundo)

            # Initial y
            y = 100
            # Initial x
            x = (window.get_width()) // 2
            # Titleself.
            surface = self.titleFont.render("Vale dos Cultivos", True, 'white')
            surface_frame = pygame.Surface((surface.get_width()+10, surface.get_height()+10))
            surface_frame.fill('black')
            surface_frame = pygame.Surface.convert_alpha(surface_frame)
            surface_frame.set_alpha(150)
            surface_frame_rect = surface_frame.get_rect(center=(x,y))
            window.blit(surface_frame, surface_frame_rect)

            
            surface_rect = surface.get_rect(center=(x+5,y))
            window.blit(surface, surface_rect)
            y += (250 * surface.get_height()) // 100
            
            # Draw menu items
            x = (window.get_width()) // 2
            if self.__opcoes_audio_ativa:
                self.__menuItemsAtual = self.menuAudioItems
            else:
                self.__menuItemsAtual = self.menuPrincipalItems

            for index, item in enumerate(self.__menuItemsAtual):
                
                # Cursor
                if index == self.currentMenuItem:
                    item['surface'] = self.itemFont.render(item['title'], True, 'cyan')
                else:
                    item['surface'] = self.itemFont.render(item['title'], True, 'white')
                
                # Item text
                surface_frame = pygame.Surface((item['surface'].get_width()+10, item['surface'].get_height()+10))
                surface_frame.fill('black')
                surface_frame = pygame.Surface.convert_alpha(surface_frame)
                surface_frame.set_alpha(150)
                surface_frame_rect = surface_frame.get_rect(center=(x,y))
                window.blit(surface_frame, surface_frame_rect)

                surface = item['surface']
                surface_rect = surface.get_rect(center=(x+5,y))
                window.blit(surface, surface_rect)

                y += (150 * surface.get_height()) // 100
        else:
            window.blit(self.__tela_instrucao, (0,0))