from abc import ABC, abstractmethod


class IControladorMenus(ABC):

    @abstractmethod
    def __init__(self):
        self.__menus = {}

    @abstractmethod
    def inclui_menu(self, menu):
        pass

    @abstractmethod
    def desenha_menu(self, id_menu):
        pass