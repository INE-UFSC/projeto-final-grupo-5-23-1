from Interfaces.IControladorMapas import IControladorMapas

class ControladorMapas(IControladorMapas):

    def __init__(self):
        super().__init__()

    @property
    def mapas(self):
        return super().__mapas
    
    def inclui_mapa(self, mapa: IMapa):
        if isinstance(mapa, IMapa):
            super().__mapas[mapa.id] = mapa
        return
    
    def desenha_mapa(self, id_mapa: str):
        self.mapas[id_mapa].desenha()
        return
