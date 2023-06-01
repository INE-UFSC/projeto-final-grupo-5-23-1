from pygame.math import Vector2


from menus.ClassesAbstratas.MenuGenerico import MenuGenerico
'''
Esta classe representa o estado de jogo de um certo modo de jogo
'''
class EstadoJogo():
    def __init__(self):
        self.epoch = 0
        self.__tamanho_mapa = Vector2(64,64)
        self.__menu_ingame_ativo = False
        self.__menu_ingame = None
        self.__observadores = [ ]

    def desativa_menu(self):
        self.__menu_ingame_ativo = False
        self.__menu_ingame = None
        return
    
    def ativa_menu(self, menu: MenuGenerico, observador):
        self.__menu_ingame = menu
        self.__menu_ingame.adiciona_observador(observador)
        self.__menu_ingame_ativo = True
        return

    @property
    def menu_ingame(self):
        return self.__menu_ingame
    
    @menu_ingame.setter
    def menu_ingame(self, menu_ingame: MenuGenerico):
        self.__menu_ingame = menu_ingame
        return

    @property
    def menu_ingame_ativo(self):
        return self.__menu_ingame_ativo
    
    @menu_ingame_ativo.setter
    def menu_ingame_ativo(self, menu_ingame_ativo: bool):
        self.__menu_ingame_ativo = menu_ingame_ativo

    @property
    def largura_mundo(self):
        """
        Retorna a largura do mapa como um inteiro
        """
        return int(self.__tamanho_mapa.x)
    
    @property
    def altura_mundo(self):
        """
        Retorna a altura do mapa como um inteiro
        """
        return int(self.__tamanho_mapa.y)        

    
    def adiciona_observador(self,observador):
        """
        Adiciona um observador ao estado de jogo
        Um observador comum ao estado de jogo é o mapa
        """
        self.__observadores.append(observador)
