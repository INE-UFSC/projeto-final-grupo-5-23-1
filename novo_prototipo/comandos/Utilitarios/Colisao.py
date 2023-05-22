import pygame

class Colisao():
    def checa_colisao(self, matriz_mapa, retangulo_nova_posicao):
        colidiu = False
        for y in range(len(matriz_mapa)):
            for x in range(len(matriz_mapa[0])):
                bloco = matriz_mapa[y][x]
                if bloco.colisao and pygame.sprite.collide_rect(retangulo_nova_posicao, bloco):
                    colidiu = True
        return colidiu