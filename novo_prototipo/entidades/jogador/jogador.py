import pygame

class Jogador(pygame.sprite.Sprite):

    #[TODO] - Refatorar o inventario para algo mais coeso

    def __init__(self, pos, group):
        super().__init__(group)

        # Setup Geral
        self.__image = pygame.Surface((40,80))
        self.__image.fill('red')
        self.__rect = self.__image.get_rect(midbottom= pos)
        
        # Colisao
        #self.__hitbox = self.rect.copy().inflate()


        # Movimentação
        self.__status = 'baixo' # Refere-se a direção que o player está olhando
        self.__posicao = pygame.math.Vector2(self.__rect.midbottom) #Troquei de .center para .midBottom para facilitar o comando de interagir
        self.__velocidade = 200
        self.__item_atual = 'enxada'

    def atualiza_status(self, status):
        self.__status = status
        return
    
    def atualiza_posicao(self, posicao):
        
        self.__posicao.x = posicao.x
        self.__posicao.y = posicao.y
        self.__rect.midbottom = posicao
        return

    def update_timers(self):
        for timer in self.__timers.values():
            timer.update()

    def update(self):
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
    def posicao_matriz(self):
        posicao_matriz = [self.__posicao.x, self.__posicao.y]
        for index, posicao in enumerate(posicao_matriz):
            posicao_matriz[index] = int(posicao // 64)
        return posicao_matriz
    
    @property
    def velocidade(self):
        return self.__velocidade
    
    @property
    def item_atual(self):
        return self.__item_atual