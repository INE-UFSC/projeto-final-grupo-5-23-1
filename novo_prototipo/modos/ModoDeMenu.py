from .ClassesAbstratas.ModoGenerico import ModoGenerico

import pygame
'''
Esta classe implementa o modo de jogo Menu, o qual tem os métodos
"checa_eventos", "update", "render";
'''
class ModoDeMenu(ModoGenerico):
    def __init__(self):        
        super().__init__()
        # Font
        self.titleFont = pygame.font.Font("novo_prototipo/assets/ui/font.ttf", 56)
        self.itemFont = pygame.font.Font("novo_prototipo/assets/ui/font.ttf", 90)
        
        # Menu items
        self.menuItems = [
            {
                'title': 'Jogar',
                'action': lambda: self.notifyShowGameRequested()
            },
            {
                'title': 'Quit',
                'action': lambda: self.notifyQuitRequested()
            }
        ]        

        # Compute menu width
        self.menuWidth = 0
        for item in self.menuItems:
            surface = self.itemFont.render(item['title'], True, 'white')
            self.menuWidth = max(self.menuWidth, surface.get_width())
            item['surface'] = surface  
        
        self.currentMenuItem = 0      

    def checa_eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.notifyQuitRequested()
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE :
                    self.notifyShowGameRequested()
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if self.currentMenuItem < len(self.menuItems) - 1:
                        self.currentMenuItem += 1
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    if self.currentMenuItem > 0:
                        self.currentMenuItem -= 1
                elif event.key == pygame.K_RETURN or event.key == pygame.K_e:
                    menuItem = self.menuItems[self.currentMenuItem]
                    try:
                        menuItem['action']()
                    except Exception as ex:
                        print(ex)
                    
    def update(self):
        pass
        
    def render(self, window):
        # Initial y
        y = 100
        
        # Title
        surface = self.titleFont.render("Vale dos Cultivos", True, 'white')
        x = (window.get_width() - surface.get_width()) // 2
        window.blit(surface, (x, y))
        y += (250 * surface.get_height()) // 100
        
        # Draw menu items
        x = (window.get_width() - self.menuWidth) // 2
        for index, item in enumerate(self.menuItems):
            
            # Cursor
            if index == self.currentMenuItem:
                item['surface'] = self.itemFont.render(item['title'], True, 'cyan')
            else:
                item['surface'] = self.itemFont.render(item['title'], True, 'white')
            
            # Item text
            surface = item['surface']
            window.blit(surface, (x, y))

            y += (200 * surface.get_height()) // 100      