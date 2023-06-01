from comandos.Comando import Comando


class ComandoAbrirMenu(Comando):
    
    def __init__(self, menu, modo_de_jogo) -> None:
        self.__modo_de_jogo = modo_de_jogo
        self.__menu = menu

    def run(self):
        self.__modo_de_jogo.ativa_menu(self.__menu, self.__modo_de_jogo)
        return