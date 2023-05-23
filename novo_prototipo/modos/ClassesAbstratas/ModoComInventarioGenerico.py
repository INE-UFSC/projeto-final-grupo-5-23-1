from modos.ClassesAbstratas.ModoGenerico import ModoGenerico

class ModoComInventarioGenerico(ModoGenerico):

    def __init__(self):
        super().__init__()
    
    def notifyShowInventoryRequested(self, inventario, jogador):
        for observador in self.observadores:
            observador.showInventoryRequested(inventario, jogador)