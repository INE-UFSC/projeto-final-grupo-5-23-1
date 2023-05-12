import pygame

from Interfaces import IControladorEventos
from Interfaces import IControladorMapas
from Interfaces import IControladorMenus

class Jogo:

    def __init__(self, controlador_eventos: IControladorEventos, controlador_mapas : IControladorMapas, controlador_menus: IControladorMenus):
        
        #Pygame:
        pygame.init()
        self.__tela = pygame.display.set_mode((1280, 720))
        self.__clock = pygame.time.Clock()
        pygame.display.set_caption('Fazendinha')

        #Controladores:
        self.__controlador_eventos = controlador_eventos
        self.__controlador_mapas = controlador_mapas
        self.__controlador_menus = controlador_menus
        
        #Dados relevantes:            
        self.__id_mapa_atual = 'campo'
        self.__id_menu_atual = 'principal'
        self.__em_jogo = True
        self.__pausa = False

    def __checa_eventos(self):
        self.__controlador_eventos.checa_eventos()
        return
    
    def __desenha_mapa(self, id_mapa: str, tela):
        self.__controlador_mapas.desenha_mapa(id_mapa, tela)
        return
    
    def __desenha_menu(self, id_menu: str):
        self.__controlador_menus.desenha_menu(id_menu)
        return
    
    def iniciar(self):
        while True:
            self.__checa_eventos()
            if self.__em_jogo:
                if self.__pausa:
                    self.__desenha_menu(self.__id_menu_atual)
                else:
                    self.__desenha_mapa(self.__id_mapa_atual, self.__tela)
            else:
                self.__desenha_menu(self.__id_menu_atual)
            pygame.display.update()
            self.__clock.tick(60) #60 Quadros por segundo

