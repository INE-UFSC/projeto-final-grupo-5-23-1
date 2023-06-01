from menus.ClassesAbstratas.MenuGenerico import MenuGenerico
from estado.ClassesAbstratas.IEstadoJogo import IEstadoJogo
'''
Esta classe representa o estado de jogo de um certo modo de jogo
'''
class EstadoJogo(IEstadoJogo):
    def __init__(self):
        super().__init__()

    def desativa_menu(self):
        self.menu_ingame_ativo = False
        self.menu_ingame = None
        return
    
    def ativa_menu(self, menu: MenuGenerico, observador):
        self.menu_ingame = menu
        self.menu_ingame.adiciona_observador(observador)
        self.menu_ingame_ativo = True
        return
