from Mapa.MapaFloresta import MapaFloresta
from Mapa.MapaSavana import MapaSavana
from menus.ClassesAbstratas.MenuGenerico import MenuGenerico
import pygame

class ControleMapa:
    def __init__(self, observador):
        self.__observador = observador
        self.__mapas = {
            "Floresta" : MapaFloresta(self),
            "Savana" : MapaSavana(self)
        }

        self.__mapa_atual = self.__mapas['Floresta']
        self.__jogador = self.__mapa_atual.jogador

    def __atualizar_mapa(self, novo_mapa):
        self.__mapa_anterior = self.__mapa_atual
        self.__mapa_atual = self.__mapas[novo_mapa]
    
    def __atualizar_jogador(self):
        self.__jogador = self.__mapa_atual.jogador
    
    def __salvar_dados_jogador(self):
        self.__inventario = self.__jogador.inventario

    def __carregar_dados_jogador(self):
        self.__jogador.set_inventario(self.__inventario)
        self.__jogador.atualiza_posicao(self.__mapa_atual.spawns[self.__mapa_anterior.id])

    
    def trocar_mapa_atual(self, novo_mapa):
        self.__salvar_dados_jogador()
        self.__atualizar_mapa(novo_mapa)
        self.__atualizar_jogador()
        self.__carregar_dados_jogador()
        self.observador.set_jogador(self.mapa_atual.jogador)

    def notifica_ativa_menu(self, menu: MenuGenerico):
        self.__observador.ativa_menu(menu, self.__observador)



    @property
    def observador(self):
        return self.__observador
    
    @property
    def mapas(self):
        return self.__mapas
    
    @property
    def mapa_atual(self):
        return self.__mapa_atual
