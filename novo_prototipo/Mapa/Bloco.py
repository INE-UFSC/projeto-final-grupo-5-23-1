from pygame import Surface
import pygame
from abc import ABC, abstractmethod


class Bloco(ABC):
    def __init__(self, x, y, largura, altura):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura

    @abstractmethod
    def desenhar(self, tela: Surface):
        pass