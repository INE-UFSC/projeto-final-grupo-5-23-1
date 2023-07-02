import pygame

class Colisao():
    def checa_colisao(self, grupoBlocos, retangulo_nova_posicao):
        colidiu = False
        for bloco in grupoBlocos.sprites():
            hitbox_bloco = pygame.sprite.Sprite(pygame.sprite.Group())
            try:
                hitbox_bloco.rect = bloco.hitbox.copy()
            except:
                hitbox_bloco.rect = bloco.rect.copy()
            if bloco.colisao and pygame.sprite.collide_rect(retangulo_nova_posicao, hitbox_bloco):
                colidiu = True
            hitbox_bloco.kill()
        return colidiu