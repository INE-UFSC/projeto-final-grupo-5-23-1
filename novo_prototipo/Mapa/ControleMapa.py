from Mapa.MapaFloresta import MapaFloresta
from Mapa.MapaDeserto import MapaDeserto
from Mapa.MapaPlanicie import MapaPlanicie
from Mapa.MapaNeve import MapaNeve
from Mapa.MapaCaverna import MapaCaverna
from Mapa.MapaTransporte import MapaTransporte
from menus.ClassesAbstratas.MenuGenerico import MenuGenerico
from Mapa.Blocos.Barreira import Barreira
from Mapa.Blocos.Grama import BlocoDeGrama
from Mapa.Blocos.Chao import Chao
import pygame

class ControleMapa:
    def __init__(self, observador):
        self.__observador = observador
        self.__mapas = {
            'Floresta' : MapaFloresta(self),
            'Deserto' : MapaDeserto(self),
            'Planicie' : MapaPlanicie(self),
            'Neve' : MapaNeve(self),
            'Caverna' : MapaCaverna(self),
            'Transporte' : MapaTransporte(self,tamanho=39)
        }

        self.__mapa_atual = None #self.__mapas['Floresta']
        self.__atualizar_mapa('Floresta')
        self.__jogador = self.__mapa_atual.jogador

    def __atualizar_mapa(self, novo_mapa):
        self.__mapa_anterior = self.__mapa_atual
        self.__mapa_atual = self.__mapas[novo_mapa]
        self.__mapa_atual.tocar_musica()
    
    def __atualizar_jogador(self):
        self.__jogador = self.__mapa_atual.jogador
    
    def __salvar_dados_jogador(self):
        self.__inventario = self.__jogador.inventario
        self.__moedas = self.__jogador.moedas

    def __carregar_dados_jogador(self):
        self.__jogador.set_inventario(self.__inventario)
        self.__jogador.set_moedas(self.__moedas)
        try:
            self.__jogador.atualiza_posicao(self.__mapa_atual.spawns[self.__mapa_anterior.id])
        except KeyError:
            self.__jogador.atualiza_posicao(self.__mapa_atual.spawns['Default'])

    
    def trocar_mapa_atual(self, novo_mapa):
        self.__salvar_dados_jogador()
        self.__atualizar_mapa(novo_mapa)
        self.__atualizar_jogador()
        self.__carregar_dados_jogador()
        self.observador.set_jogador(self.mapa_atual.jogador)

    def notifica_ativa_menu(self, menu: MenuGenerico):
        self.__observador.ativa_menu(menu, self.__observador)
    
    def desbloquear_mapa(self, mapa):
        for map in self.__mapas.values():
            for grupo in map.grupos:
                for entidade in grupo:
                    if isinstance(entidade, Barreira) and entidade.mapa == mapa:
                        grupo.remove(entidade)
                        
                        # Trocar os blocos de barreira por outros
                        if map.id == 'Transporte':
                            bloco = Chao(entidade.pos, entidade.surf, [map.grupoAll, map.grupoBlocos], map)
                        else:
                            bloco = BlocoDeGrama(entidade.pos, entidade.surf, [map.grupoAll, map.grupoBlocos], map, True)
                        map.troca_bloco(entidade.posicao_matriz[0],entidade.posicao_matriz[1], bloco)



    @property
    def observador(self):
        return self.__observador
    
    @property
    def mapas(self):
        return self.__mapas
    
    @property
    def mapa_atual(self):
        return self.__mapa_atual
