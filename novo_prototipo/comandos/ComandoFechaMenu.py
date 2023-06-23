from comandos.Comando import Comando


class ComandoFechaMenu(Comando):
    
    def __init__(self, menu) -> None:
        self.__menu = menu

    def run(self):
        self.__menu.notifica_desativa_menu()
        return