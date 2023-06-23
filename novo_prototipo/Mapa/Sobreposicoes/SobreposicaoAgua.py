import pygame

from settings import LAYERS


class SobreposicaoAgua(pygame.sprite.Sprite):

    def __init__(self, posicao) -> None:
        super().__init__()
        self.__image = pygame.transform.scale(pygame.image.load('novo_prototipo/assets/ui/sobreposicaoAgua_TESTE.png'), (64, 64))
        self.__image.set_alpha(128)
        self.__rect_image = self.__image.get_rect(topleft=posicao)
        self.__z = LAYERS['sobreposicao_bloco']

        self.__nascimento = pygame.time.get_ticks() / 1000
        self.__duracao = 50

    @property
    def image(self):
        return self.__image

    @property
    def rect(self):
        return self.__rect_image
    
    @property
    def z(self):
        return self.__z

    @property
    def duracao(self):
        return self.__duracao

    @property
    def nascimento(self):
        return self.__nascimento