import pygame
from entidades.jogador.timer import Timer

class Jogador(pygame.sprite.Sprite):

    #[TODO] - Refatorar o inventario para algo mais coeso

    def __init__(self, pos, group):
        super().__init__(group)

        # Setup Geral
        self.__image = pygame.Surface((40,80))
        self.__image.fill('red')
        self.__rect = self.__image.get_rect(center= pos)
        
        # Colisao
        #self.__hitbox = self.rect.copy().inflate()


        # Movimentação
        self.__status = 'baixo' # Refere-se a direção que o player está olhando
        self.__direcao = pygame.math.Vector2()
        self.__posicao = pygame.math.Vector2(self.__rect.center)
        self.__velocidade = 200
        
        # Timers
        self.__timers = {
            'usar ferramenta': Timer(350, self.usar_ferramenta),
            'trocar ferramenta': Timer(200),
            'usar semente': Timer(350, self.usar_semente),
            'trocar semente': Timer(200),
        }

        self.__item_atual = 'enxada'

    def atualiza_status(self, status):
        self.__status = status
        return
    
    def atualiza_posicao(self, posicao):
        self.__posicao.x = posicao.x
        self.__posicao.y = posicao.y
        self.__rect.centerx = round(posicao.x)
        self.__rect.centery = round(posicao.y)
        return

    def update_timers(self):
        for timer in self.__timers.values():
            timer.update()

    def update(self):
        self.get_pos_alvo()
        self.update_timers()

    @property    
    def status(self):
        return self.__status
    
    @property
    def image(self):
        return self.__image
    
    @property
    def rect(self):
        return self.__rect
    
    @property
    def posicao(self):
        return self.__posicao
    
    @property
    def velocidade(self):
        return self.__velocidade
    
    @property
    def item_atual(self):
        return self.__item_atual