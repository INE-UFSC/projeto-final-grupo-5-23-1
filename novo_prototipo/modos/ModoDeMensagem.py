from modos.ClassesAbstratas.ModoGenerico import ModoGenerico

import pygame
'''
Esta classe implementa o modo de jogo Mensagem, o qual tem os métodos
"checa_eventos", "update", "render";
'''
class ModoDeMensagem(ModoGenerico):
    def __init__(self, mensagem):     
        super().__init__()
        self.__fonte = pygame.font.Font("novo_prototipo/assets/ui/font.ttf", 36)
        self.__mensagem = mensagem

    def checa_eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.notifyQuitRequested()
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    self.notifyShowMenuRequested()
                    
    def update(self):
        pass
        
    def render(self, window):
        surface = self.__fonte.render(self.__mensagem, True, 'white')
        x = (window.get_width() - surface.get_width()) // 2
        y = (window.get_height() - surface.get_height()) // 2
        window.blit(surface, (x, y))