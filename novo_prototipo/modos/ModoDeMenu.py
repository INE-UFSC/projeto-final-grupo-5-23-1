from .ClassesAbstratas.ModoGenerico import ModoGenerico
import pygame
import os

dir_atual = os.path.dirname(os.path.abspath(__file__))
pasta_assets = os.path.join(dir_atual, '..', 'assets', 'ui')
caminho_fundo = os.path.join(pasta_assets, 'fundo_menu_pause.png')
caminho_fonte = os.path.join(pasta_assets, 'font.ttf')
'''
Esta classe implementa o modo de jogo Menu, o qual tem os métodos
"checa_eventos", "update", "render";
'''
class ModoDeMenu(ModoGenerico):
    def __init__(self):        
        super().__init__()
        # Font
        self.titleFont = pygame.font.Font(caminho_fonte, 56)
        self.itemFont = pygame.font.Font(caminho_fonte, 90)
        self.__fundo = pygame.image.load(caminho_fundo).convert_alpha()
        self.__fundo.set_alpha(150)
        self.__opcoes_audio_ativa = False
        
        # Menu items
        self.menuPrincipalItems = [
            {
                'title': 'Continuar',
                'action': lambda: self.notifyShowGameRequested()
            },
            {
                'title': 'Áudio',
                'action': lambda: self.mostra_opcoes_audio()
            },
            {
                'title': 'Voltar',
                'action': lambda: self.notifica_ativa_menu_principal()
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

    def checa_eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.notifyQuitRequested()
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if self.currentMenuItem < len(self.__menuItemsAtual) - 1:
                        self.currentMenuItem += 1
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    if self.currentMenuItem > 0:
                        self.currentMenuItem -= 1
                if event.key == pygame.K_RETURN or event.key == pygame.K_e:
                    menuItem = self.__menuItemsAtual[self.currentMenuItem]
                    try:
                        if self.currentMenuItem != 0 or not self.__opcoes_audio_ativa:
                            menuItem['action']()
                    except Exception as ex:
                        print(ex)
                    self.currentMenuItem = 0

                if self.currentMenuItem == 0 and self.__opcoes_audio_ativa:
                    if event.key == pygame.K_RIGHT:
                        menuItem = self.__menuItemsAtual[self.currentMenuItem]
                        menuItem['action1']()
                    elif event.key == pygame.K_LEFT:
                        menuItem = self.__menuItemsAtual[self.currentMenuItem]
                        menuItem['action2']()

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
        window.blit(self.__fundo, (0, 0))
        y = 250
        
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

            surface = item['surface']
            surface_rect = surface.get_rect(center=(x+5,y))
            window.blit(surface, surface_rect)

            y += (150 * surface.get_height()) // 100