import copy

import pygame
from .Comando import Comando
from pygame.math import Vector2
from comandos.Utilitarios.Colisao import Colisao

class ComandoMover(Comando):
    """
    Esse comando move uma unidade implementando também 
    as limitações do movimento
    """
    def __init__(self, grupoBlocos, entidade, direcao, status, delta_tempo):
        self.__grupoBlocos = grupoBlocos
        self.__entidade = entidade
        self.__direcao = Vector2()
        self.__adiciona_direcao(direcao)
        self.__status = status
        self.__delta_tempo = delta_tempo
        self.__verificar_colisao = Colisao()

    def __adiciona_direcao(self, direcao):
        if direcao.magnitude() > 0:
            self.__direcao = direcao.normalize()
        return
    
    def __checa_colisao(self, grupoBlocos, retangulo_nova_posicao):
        return self.__verificar_colisao.checa_colisao(grupoBlocos, retangulo_nova_posicao)

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

        # Manter o jogador no centro da tela
        centro_tela = Vector2(pygame.display.get_surface().get_size()) / 2
        deslocamento = centro_tela - nova_posicao
        nova_posicao += deslocamento

        entidade_nova_posicao = pygame.sprite.Sprite(pygame.sprite.Group())
        entidade_nova_posicao.rect = self.__entidade.rect.copy()
        entidade_nova_posicao.rect.midbottom = nova_posicao

        if self.__checa_colisao(self.__grupoBlocos, entidade_nova_posicao):
            entidade_nova_posicao.kill()
            return
        else:
            entidade_nova_posicao.kill()
            unit.atualiza_posicao(nova_posicao)
        