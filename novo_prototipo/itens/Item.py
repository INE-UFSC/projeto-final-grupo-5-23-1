from abc import ABC, abstractmethod

import pygame

class Item(ABC):
    @abstractmethod
    def __init__(self, nome, preco, caminho_imagem: str):
        self.__nome = nome
        self.__preco = preco
        self.__imagem = pygame.image.load(caminho_imagem)

    @property
    def nome(self):
        return self.__nome
    
    @property
    def preco(self):
        return self.__preco
    
    @property
    def imagem(self):
        return self.__imagem