import pygame
from entidades.jogador.jogador import Jogador
from pytmx.util_pygame import load_pygame
from Mapa.Blocos.Parede import Parede
from Mapa.Blocos.Chao import Chao
from Mapa.Blocos.Transporte import Transporte
from Mapa.interfaces.IMapa import IMapa

class MapaTransporte(IMapa):
    def __init__(self, observador, tamanho):
        super().__init__(observador, tamanho)
        self.__id = 'Transporte'
    
    @property
    def id(self):
        return self.__id
    
    def construir_blocos(self):
        tmx_data = load_pygame('novo_prototipo/Mapa/Mapas/transporte.tmx')
        
        for layer in tmx_data.layers:
            if layer.name  == 'Fundo':
                for x, y, surf in layer.tiles():
                    pos = (x*64, y*64)
                    bloco = Parede(pos= pos, surf= surf, groups= [self.grupoAll, self.grupoBlocos], observador=self)
                    self.blocos[y][x] = bloco

            if layer.name == 'Chao':
                for x, y, surf in layer.tiles():
                    pos = (x*64, y*64)
                    bloco = Chao(pos= pos, surf= surf, groups= [self.grupoAll, self.grupoBlocos], observador= self)
                    self.blocos[y][x] = bloco
            
            if layer.name == 'TpFloresta':
                for x, y, surf in layer.tiles():
                    pos = (x*64, y*64)
                    bloco = Transporte(pos= pos, surf= surf, groups= [self.grupoAll, self.grupoBlocos], observador= self, mapa='Floresta')
                    self.blocos[y][x] = bloco

            if layer.name == 'TpDeserto':
                for x, y, surf in layer.tiles():
                    pos = (x*64, y*64)
                    bloco = Transporte(pos= pos, surf= surf, groups= [self.grupoAll, self.grupoBlocos], observador= self, mapa='Deserto')
                    self.blocos[y][x] = bloco
            
            if layer.name == 'TpNeve':
                for x, y, surf in layer.tiles():
                    pos = (x*64, y*64)
                    bloco = Transporte(pos= pos, surf= surf, groups= [self.grupoAll, self.grupoBlocos], observador= self, mapa='Neve')
                    self.blocos[y][x] = bloco
            
            if layer.name == 'TpPlanicie':
                for x, y, surf in layer.tiles():
                    pos = (x*64, y*64)
                    bloco = Transporte(pos= pos, surf= surf, groups= [self.grupoAll, self.grupoBlocos], observador= self, mapa='Planicie')
                    self.blocos[y][x] = bloco

            if layer.name == 'TpCaverna':
                for x, y, surf in layer.tiles():
                    pos = (x*64, y*64)
                    bloco = Transporte(pos= pos, surf= surf, groups= [self.grupoAll, self.grupoBlocos], observador= self, mapa='Caverna')
                    self.blocos[y][x] = bloco
            
            if layer.name == 'Spawns':
                for obj in layer:
                    self.spawns[obj.name] = pygame.math.Vector2(obj.x, obj.y)
    
    def adiciona_entidades(self):
        self.entidades.append(Jogador(self.spawns['Default'], [self.grupoAll, self.grupoJogador]))

    def tocar_musica(self):
        pygame.mixer.music.stop()        
        pygame.mixer.init()
        pygame.mixer.music.load("./novo_prototipo/trilha/trilha_transporte.mp3")
        pygame.mixer.music.play(-1)