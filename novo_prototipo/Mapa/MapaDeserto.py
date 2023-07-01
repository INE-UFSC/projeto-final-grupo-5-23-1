from entidades.jogador.jogador import Jogador
from pytmx.util_pygame import load_pygame
from Mapa.Blocos.Grama import BlocoDeGrama
from Mapa.Blocos.Parede import Parede
from Mapa.Blocos.Transporte import Transporte
from Mapa.Blocos.Barreira import Barreira
from Mapa.Blocos.Chao import Chao
from entidades.vendedor import Vendedor
from Mapa.interfaces.IMapa import IMapa
import pygame

from Mapa.Climas.climas.ClimaDeserto import ClimaDeserto

class MapaDeserto(IMapa):
    def __init__(self, observador):
        super().__init__(observador, clima=ClimaDeserto())
        self.id = 'Deserto'

    def construir_blocos(self):
        tmx_data = load_pygame('novo_prototipo/Mapa/Mapas/deserto.tmx')
        
        for layer in tmx_data.layers:
            if layer.name  == 'Fundo':
                for x, y, surf in layer.tiles():
                    pos = (x*64, y*64)
                    bloco = Parede(pos= pos, surf= surf, groups= [self.grupoAll, self.grupoBlocos], observador=self)
                    self.blocos[y][x] = bloco

            if layer.name == 'Grama':
                for x, y, surf in layer.tiles():
                    pos = (x*64, y*64)
                    bloco = BlocoDeGrama(pos= pos, surf= surf, groups= [self.grupoAll, self.grupoBlocos], observador= self)
                    self.blocos[y][x] = bloco
            
            if layer.name == 'Chao':
                for x, y, surf in layer.tiles():
                    pos = (x*64, y*64)
                    bloco = Chao(pos= pos, surf= surf, groups= [self.grupoAll, self.grupoBlocos], observador= self)
                    self.blocos[y][x] = bloco

            if layer.name == 'Vendedor':
                for obj in layer:
                    bloco = Vendedor(pos= (obj.x, obj.y), surf= obj.image, groups= [self.grupoAll, self.grupoBlocos], observador= self, mapa= 'Deserto')

                    x = int(obj.x // 64)
                    y = int(obj.y // 64)
                    self.blocos[y][x] = bloco
            
            if layer.name == 'Tps':
                for obj in layer:
                    if obj.name == 'Transporte':
                        bloco = Transporte(pos= (obj.x,obj.y), surf= obj.image, groups= [self.grupoAll, self.grupoBlocos], observador= self, mapa='Transporte')
                    if obj.name == 'Planicie':
                        bloco = Transporte(pos= (obj.x,obj.y), surf= obj.image, groups= [self.grupoAll, self.grupoBlocos], observador= self, mapa='Planicie')
                    if obj.name == 'Floresta':
                        bloco = Transporte(pos= (obj.x,obj.y), surf= obj.image, groups= [self.grupoAll, self.grupoBlocos], observador= self, mapa= 'Floresta')
                    
                    x = int(obj.x // 64)
                    y = int(obj.y // 64)

                    self.blocos[y][x] = bloco

            if layer.name == 'Barreiras':
                for obj in layer:
                    if obj.name == 'Transporte':
                        bloco = Barreira(pos= (obj.x,obj.y), surf= obj.image, groups= [self.grupoAll, self.grupoBlocos], observador= self, mapa='Transporte')
                    if obj.name == 'Planicie':
                        bloco = Barreira(pos= (obj.x,obj.y), surf= obj.image, groups= [self.grupoAll, self.grupoBlocos], observador= self, mapa='Planicie')
                    
                    x = int(obj.x // 64)
                    y = int(obj.y // 64)

                    self.blocos[y][x] = bloco
    
            if layer.name == 'Spawns':
                for obj in layer:
                    self.spawns[obj.name] = pygame.math.Vector2(obj.x, obj.y)
                    
    def adiciona_jogador(self):
        self.entidades.append(Jogador(self.spawns['Default'], [self.grupoAll, self.grupoJogador]))

    def tocar_musica(self):
        pygame.mixer.music.stop()        
        
        pygame.mixer.music.load("./novo_prototipo/trilha/trilha_deserto.mp3")
                
        pygame.mixer.music.play(-1)