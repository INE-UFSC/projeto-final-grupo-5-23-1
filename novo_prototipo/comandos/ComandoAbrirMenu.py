from comandos.Comando import Comando


class ComandoAbrirMenu(Comando):
    
    def __init__(self, estado_jogo, menu, observador_menu) -> None:
        self.__estado_jogo = estado_jogo
        self.__menu = menu
        self.__observador_menu = observador_menu

    def run(self):
        self.__estado_jogo.menu_ingame = self.__menu
        self.__estado_jogo.menu_ingame.adiciona_observador(self.__observador_menu)
        self.__estado_jogo.menu_ingame_ativo = True
        return