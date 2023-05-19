import pygame
from entidades.jogador.timer import Timer

class Jogador(pygame.sprite.Sprite):
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

        # Ferramentas
        self.__ferramentas = ['enxada', 'agua', 'machado', 'picareta']
        self.__index_ferramenta = 0
        self.__ferramenta_atual = self.__ferramentas[self.__index_ferramenta]

        # Sementes
        self.__sementes = ['milho', 'feijao']
        self.__index_semente = 0
        self.__semente_atual = self.__sementes[self.__index_semente]

    def atualiza_status(self, status):
        self.__status = status
        return
    
    def atualiza_posicao(self, posicao):
        self.__posicao.x = posicao.x
        self.__posicao.y = posicao.y
        self.__rect.centerx = round(posicao.x)
        self.__rect.centery = round(posicao.y)
        return

    def input(self):
        keys = pygame.key.get_pressed()
        
        # Ferramentas
        if keys[pygame.K_SPACE]:
            self.__timers['usar ferramenta'].ativar()
            self.__direcao = pygame.math.Vector2() # Fazer o player parar no lugar

        if keys[pygame.K_q] and not self.__timers['trocar ferramenta'].ativado:
            self.__timers['trocar ferramenta'].ativar()
            self.__index_ferramenta += 1
            self.__index_ferramenta = self.__index_ferramenta if self.__index_ferramenta < len(self.__ferramentas) else 0
            self.__ferramenta_atual = self.__ferramentas[self.__index_ferramenta]

        # Sementes
        if keys[pygame.K_LCTRL]:
            self.__timers['usar semente'].ativar()
            self.__direcao = pygame.math.Vector2()

        if keys[pygame.K_e] and (self.__timers['trocar semente'].ativado == False):
            self.__timers['trocar semente'].ativar()
            self.__index_semente += 1
            self.__index_semente = self.__index_semente if self.__index_semente < len(self.__sementes) else 0
            self.__semente_atual = self.__sementes[self.__index_semente]

    def usar_semente(self):
        pass

    def usar_ferramenta(self):
        if self.__ferramenta_atual == 'enxada':
            pass

        elif self.__ferramenta_atual == 'agua':
            pass

        elif self.__ferramenta_atual == 'machado':
            pass

        elif self.__ferramenta_atual == 'picareta':
            pass
    
    def get_pos_alvo(self):
        self.__alvo_pos = self.rect.center + self.get_offset()
    
    def get_offset(self):
        offsets = {
            'esquerda': pygame.math.Vector2(-50,40),
            'direita': pygame.math.Vector2(50,40),
            'cima': pygame.math.Vector2(0,-10),
            'baixo': pygame.math.Vector2(0,50)
        }
        return offsets[self.__status]

    def update_timers(self):
        for timer in self.__timers.values():
            timer.update()

    def update(self):
        self.get_pos_alvo()
        self.update_timers()

        
    
    @property
    def image(self):
        return self.__image
    
    @property
    def rect(self):
        return self.__rect
    
    @property
    def ferramenta_atual(self):
        return self.__ferramenta_atual
    
    @property
    def semente_atual(self):
        return self.__semente_atual
    
    @property
    def posicao(self):
        return self.__posicao
    
    @property
    def velocidade(self):
        return self.__velocidade