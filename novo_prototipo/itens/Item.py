from abc import ABC, abstractmethod

import pygame

class Item(ABC):
    @abstractmethod
    def __init__(self, nome, preco, caminho_imagem: str):
        self.__nome = nome
        self.__preco = preco
        self.__imagem = pygame.transform.scale(pygame.image.load(caminho_imagem), (72, 72))

    @property
    def nome(self):
        return self.__nome
    
    @property
    def preco(self):
        return self.__preco
    
    def set_preco(self, preco):
        self.__preco = preco
    
    @property
    def imagem(self):
        return self.__imagem
    
    def set_imagem(self, imagem):
        self.__imagem = imagem