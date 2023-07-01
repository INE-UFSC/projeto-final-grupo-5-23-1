import pygame

class Colisao():
    def checa_colisao(self, grupoBlocos, retangulo_nova_posicao):
        colidiu = False
        for bloco in grupoBlocos.sprites():
            if bloco.colisao and pygame.sprite.collide_rect(retangulo_nova_posicao, bloco):
                colidiu = True
        return colidiu