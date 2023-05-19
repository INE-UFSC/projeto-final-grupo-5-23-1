from .Command import Comando
from pygame.math import Vector2

class MoveCommand(Comando):
    """
    Esse comando move uma unidade implementando também 
    as limitações do movimento
    """
    def __init__(self, estado, entidade, direcao, status, delta_tempo):
        self.__estado = estado
        self.__entidade = entidade
        self.__direcao = Vector2()
        self.__adiciona_direcao(direcao)
        self.__status = status
        self.__delta_tempo = delta_tempo

    def __adiciona_direcao(self, direcao):
        if direcao.magnitude() > 0:
            self.__direcao = direcao.normalize()
        return

    def run(self):
        unit = self.__entidade
        nova_posicao = Vector2()
        unit.atualiza_status(self.__status)
        
        # Movimentação Horizontal
        movimento_x = self.__direcao.x * unit.velocidade * self.__delta_tempo
        # Movimentação Vertical
        movimento_y = self.__direcao.y * unit.velocidade * self.__delta_tempo

        nova_posicao.x = unit.posicao.x + movimento_x
        nova_posicao.y = unit.posicao.y + movimento_y

        unit.atualiza_posicao(nova_posicao)
        