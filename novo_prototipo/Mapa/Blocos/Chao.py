from Mapa.Blocos.interfaces.IBloco import IBloco

class Chao(IBloco):
    def __init__(self, pos, surf, groups, observador):
        super().__init__(pos, surf, groups, observador)

    def desenhar(self, tela):
        pass
