from pygame.math import Vector2
'''
Esta classe representa o estado de jogo de um certo modo de jogo
'''
class EstadoJogo():
    def __init__(self):
        self.epoch = 0
        self.__tamanho_mapa = Vector2(64,64)
        self.__observadores = [ ]
    
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
