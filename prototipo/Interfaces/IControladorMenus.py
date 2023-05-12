from abc import ABC, abstractmethod

from pygame import Surface

from Interfaces.IMenu import IMenu


class IControladorMenus(ABC):

    @abstractmethod
    def __init__(self):
        self.__menus = {}

    @abstractmethod
    def inclui_menu(self, menu: IMenu):
        pass

    @abstractmethod
    def desenha_menu(self, id_menu: str, tela: Surface):
        pass