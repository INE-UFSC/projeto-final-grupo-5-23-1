import pygame

# Essa classe existe para criar delay entre a repetição de ações
# porque no pygame as interações são renderizadas a cada milisegundo
# então pode ocorrer repetição indevida de ações

class Timer:
    def __init__(self, duracao, funcao = None):
        self.__duracao = duracao
        self.__funcao = funcao # Função que ocorrerá após o término do timer

        self.__tempo_inicial = 0
        self.__ativado = False

    def ativar(self):
        self.__ativado = True
        self.__tempo_inicial = pygame.time.get_ticks()
    
    def desativar(self):
        self.__ativado = False
        self.__tempo_inicial = 0

    def update(self):
        tempo_atual = pygame.time.get_ticks()
        if tempo_atual - self.__tempo_inicial >= self.__duracao:
            if self.__funcao and (self.__tempo_inicial != 0):
                self.__funcao()
            self.desativar()

    @property
    def ativado(self):
        return self.__ativado