from itens.ferramentas.Ferramenta import Ferramenta


class Regador(Ferramenta):

    def __init__(self, nome='Regador', preco=15, caminho_imagem='novo_prototipo/assets/ui/regador_TESTE.png'):
        super().__init__(nome, preco, caminho_imagem)