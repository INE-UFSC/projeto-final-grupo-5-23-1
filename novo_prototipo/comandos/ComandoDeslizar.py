import pygame
from pygame.math import Vector2
from comandos import Comando

class ComandoDeslizar(Comando):
    def __init__(self, entidade, status, delta_tempo):
        self.__entidade = entidade
        self.__direcao = Vector2()
        self.__status = status
        self.__delta_tempo = delta_tempo

    def run(self):
        unit = self.__entidade
        nova_posicao = Vector2()
        if self.__status == 'direita':
            movimento_x = unit.velocidade * 3 * self.__delta_tempo
            movimento_y = 0
        
        elif self.__status == 'esquerda':
            movimento_x = unit.velocidade * -3 * self.__delta_tempo
            movimento_y = 0
        
        if self.__status == 'cima':
            movimento_x = 0
            movimento_y = unit.velocidade * -3 * self.__delta_tempo
        
        elif self.__status == 'baixo':
            movimento_x = 0
            movimento_y = unit.velocidade * 3 * self.__delta_tempo

        nova_posicao.x = unit.posicao.x + movimento_x
        nova_posicao.y = unit.posicao.y + movimento_y

        entidade_nova_posicao = pygame.sprite.Sprite(pygame.sprite.Group())
        try:
            entidade_nova_posicao.rect = self.__entidade.hitbox.copy()
        except:
            entidade_nova_posicao.rect = self.__entidade.rect.copy()
        entidade_nova_posicao.rect.midbottom = nova_posicao

        entidade_nova_posicao.kill()
        unit.atualiza_posicao(nova_posicao)
        