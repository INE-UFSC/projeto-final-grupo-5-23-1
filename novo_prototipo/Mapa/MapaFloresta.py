import pygame
from entidades.jogador.jogador import Jogador
from pytmx.util_pygame import load_pygame
from Mapa.Blocos.Grama import BlocoDeGrama
from Mapa.Blocos.Parede import Parede
from Mapa.Blocos.Transporte import Transporte
from entidades.vendedor import Vendedor
from Mapa.interfaces.IMapa import IMapa
from Mapa.Blocos.Barreira import Barreira
from Mapa.Climas.climas.ClimaFloresta import ClimaFloresta

class MapaFloresta(IMapa):
    def __init__(self, observador):
        super().__init__(observador, clima=ClimaFloresta())
        self.id = 'Floresta'

    def construir_blocos(self):
        tmx_data = load_pygame('novo_prototipo/Mapa/Mapas/floresta.tmx')
        
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
            
            if layer.name == 'Vendedor':
                for obj in layer:
                    bloco = Vendedor(pos= (obj.x, obj.y), surf= obj.image, groups= [self.grupoAll, self.grupoBlocos], observador= self, mapa= 'Floresta')

                    x = int(obj.x // 64)
                    y = int(obj.y // 64)

                    self.blocos[y][x] = bloco
            
            if layer.name == 'Tps':
                for obj in layer:
                    if obj.name == 'Transporte':
                        bloco = Transporte(pos= (obj.x,obj.y), surf= obj.image, groups= [self.grupoAll, self.grupoBlocos], observador= self, mapa='Transporte')
                    if obj.name == 'Deserto':
                        bloco = Transporte(pos= (obj.x,obj.y), surf= obj.image, groups= [self.grupoAll, self.grupoBlocos], observador= self, mapa='Deserto')
                    if obj.name == 'Neve':
                        bloco = Transporte(pos= (obj.x,obj.y), surf= obj.image, groups= [self.grupoAll, self.grupoBlocos], observador= self, mapa= 'Neve')
                    
                    x = int(obj.x // 64)
                    y = int(obj.y // 64)

                    self.blocos[y][x] = bloco
            
            if layer.name == 'Barreiras':
                for obj in layer:
                    if obj.name == 'Transporte':
                        bloco = Barreira(pos= (obj.x,obj.y), surf= obj.image, groups= [self.grupoAll, self.grupoBlocos], observador= self, mapa='Transporte')
                    if obj.name == 'Deserto':
                        bloco = Barreira(pos= (obj.x,obj.y), surf= obj.image, groups= [self.grupoAll, self.grupoBlocos], observador= self, mapa='Deserto')
                    if obj.name == 'Neve':
                        bloco = Barreira(pos= (obj.x,obj.y), surf= obj.image, groups= [self.grupoAll, self.grupoBlocos], observador= self, mapa='Neve')
                    
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
        
        pygame.mixer.music.load("./novo_prototipo/trilha/trilha_floresta.mp3")
        
        pygame.mixer.music.play(-1)      