from pygame import Surface
from Interfaces.IControladorMapas import IControladorMapas
from Interfaces.IMapa import IMapa

class ControladorMapas(IControladorMapas):

    def __init__(self):
        super().__init__()

    @property
    def mapas(self):
        return super().mapas
    
    def inclui_mapa(self, mapa: IMapa):
        if isinstance(mapa, IMapa):
            super().mapas[mapa.id] = mapa
        return
    
    def desenha_mapa(self, id_mapa: str, tela: Surface):
        self.mapas[id_mapa].desenhar(tela)
        return
