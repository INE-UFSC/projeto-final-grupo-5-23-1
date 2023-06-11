from Mapa.Blocos.interfaces.IBloco import IBloco

class Agua(IBloco):
    def __init__(self, pos, surf, groups, observador):
        super().__init__(pos, surf, groups, observador, True)

    def desenhar(self, tela):
        pass