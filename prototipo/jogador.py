import pygame

class Jogador(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        # Setup Geral
        self.__image = pygame.Surface((40,80))
        self.__image.fill('red')
        self.__rect = self.__image.get_rect(center= pos)
        
        # Colisao
        self.__hitbox = self.rect.copy().inflate()

        # Movimentação
        self.__direcao = pygame.math.Vector2()
        self.__posicao = pygame.math.Vector2(self.__rect.center)
        self.__velocidade = 200
    
    def input(self):
        keys = pygame.key.get_pressed()
        
        # Direções
        if keys[pygame.K_w]:
            self.__direcao.y = -1
            print("Cima")
        elif keys[pygame.K_s]:
            self.__direcao.y = 1
            print("Baixo")
        else:
            self.__direcao.y = 0
        
        if keys[pygame.K_d]:
            self.__direcao.x = 1
            print("Direita")
        elif keys[pygame.K_a]:
            self.__direcao.x = -1
            print('Esquerda')
        else:
            self.__direcao.x = 0
    
    def movimentar(self, dt):

        # Normalizar vetor
        if self.__direcao.magnitude() > 0:
            self.__direcao = self.__direcao.normalize()
        
        # Movimentação Horizontal
        self.__posicao.x += self.__direcao.x * self.__velocidade * dt
        self.__rect.centerx = round(self.__posicao.x)

        # Movimentação Vertical
        self.__posicao.y += self.__direcao.y * self.__velocidade * dt
        self.__rect.centery = round(self.__posicao.y)
    
    def update(self, dt):
        self.input()

        self.movimentar(dt)
        
    
    @property
    def image(self):
        return self.__image
    
    @property
    def rect(self):
        return self.__rect