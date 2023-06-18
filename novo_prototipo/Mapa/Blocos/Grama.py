from Mapa.Blocos.interfaces.IBlocoComInteracao import IBlocoComInteracao
from Mapa.Blocos.TerraArada import TerraArada
from itens.ferramentas.Enxada import Enxada

class BlocoDeGrama(IBlocoComInteracao):
    def __init__(self, pos, surf, groups, observador):
        super().__init__(pos, surf, groups, observador)
        self.__groups = groups
    
    def interagir(self, jogador):
        if isinstance(jogador.item_atual, Enxada):
            bloco = TerraArada(self.pos, self.surf, [self.observador.grupoAll, self.observador.grupoBlocos], self.observador)
            self.notifica_troca_bloco(self.posicao_matriz[0], self.posicao_matriz[1], bloco)
        
    def desenhar(self, tela):
        pass