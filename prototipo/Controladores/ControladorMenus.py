from Interfaces.IControladorMenus import IControladorMenus
from Interfaces.IMenu import IMenu

class ControladorMenus(IControladorMenus):

    def __init__(self):
        super().__init__()

    @property
    def menus(self):
        return super().__menus

    def inclui_menu(self, menu: IMenu):
        if isinstance(menu, IMenu):
            super().__menus[menu.id] = menu
        return
    
    def desenha_menu(self, id_menu: str):
        self.menus[id_menu].desenha()
