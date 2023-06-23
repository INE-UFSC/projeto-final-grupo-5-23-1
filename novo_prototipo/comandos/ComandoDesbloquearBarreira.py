from comandos import Comando


class ComandoDesbloquearBarreira(Comando):

    def __init__(self, jogador, barreira):
        self.__jogador = jogador
        self.__barreira = barreira

    def run(self):
        moedas_resultante = self.__jogador.moedas - self.__barreira.custo
        if moedas_resultante >= 0:
            self.__jogador.set_moedas(self.__jogador.moedas - self.__barreira.custo)
            self.__barreira.observador.notifica_exclui_barreira(self.__barreira.mapa)