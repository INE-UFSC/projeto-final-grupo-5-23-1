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
        #Informações para centralizar menu
        self.__tamanho_tela = list(pygame.display.get_window_size())
        self.__centro_tela = (self.__tamanho_tela[0] / 2, self.__tamanho_tela[1] / 2)

        # Font
        self.titleFont = pygame.font.Font("novo_prototipo/assets/ui/font.ttf", 56)
        self.itemFont = pygame.font.Font("novo_prototipo/assets/ui/font.ttf", 90)

        # Fundo
        self.__fundo = pygame.transform.scale(pygame.image.load("novo_prototipo/assets/ui/fundo_TESTE.png"), (1280, 768))
        self.__rect_fundo = self.__fundo.get_rect(center=self.__centro_tela)
        
        # Menu principal items
        self.menuPrincipalItems = [
            {
                'title': 'Jogar',
                'action': lambda: self.notifica_desativa_menu_principal()
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
                if event.key == pygame.K_RETURN:
                    menuItem = self.__menuItemsAtual[self.currentMenuItem]
                    try:
                        if self.currentMenuItem != 0 or not self.__opcoes_audio_ativa:
                            menuItem['action']()
                    except Exception as ex:
                        print(ex)
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
                'title': f'Volume {int(pygame.mixer.music.get_volume()*10)}',
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

        # Fundo:
        window.blit(self.__fundo, self.__rect_fundo)

        # Initial y
        y = 100
        
        # Titleself.
        surface = self.titleFont.render("Vale dos Cultivos", True, 'white')
        x = (window.get_width() - surface.get_width()) // 2
        window.blit(surface, (x, y))
        y += (250 * surface.get_height()) // 100
        
        # Draw menu items
        x = (window.get_width() - self.menuWidth) // 2
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
            surface = item['surface']
            window.blit(surface, (x, y))

            y += (200 * surface.get_height()) // 100      