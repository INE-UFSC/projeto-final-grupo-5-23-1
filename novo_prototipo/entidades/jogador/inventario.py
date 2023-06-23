from itens.Item import Item
from itens.ItemQuantizavel import ItemQuantizavel


class Inventario:
    def __init__(self, tamanho_matriz):
        self.__tamanho_matriz = tamanho_matriz
        self.__capacidade = tamanho_matriz[0] * tamanho_matriz[1]
        self.__itens = [None for _ in range(self.capacidade_maxima)]

    @property
    def itens(self):
        return self.__itens
    
    @property
    def tamanho_matriz(self):
        return self.__tamanho_matriz

    @property
    def capacidade_maxima(self):
        return self.__capacidade
    
    @property
    def capacidade_atual(self):
        quantidade_de_itens = 0
        for item in self.itens:
            if isinstance(item, Item):
                quantidade_de_itens += 1
        return quantidade_de_itens
    
    def adicionar_item(self, item_a_ser_adicionado):
        if isinstance(item_a_ser_adicionado, Item):
            if isinstance(item_a_ser_adicionado, ItemQuantizavel):
                lista_de_nomes = []
                for item in self.__itens:
                    if isinstance(item, Item):
                        lista_de_nomes.append(item.nome)
                    else:
                        lista_de_nomes.append(None)

                if item_a_ser_adicionado.nome in lista_de_nomes:
                    indice_item = lista_de_nomes.index(item_a_ser_adicionado.nome)
                    self.__itens[indice_item].aumenta_quantidade(item_a_ser_adicionado.quantidade)
                elif self.capacidade_atual < self.capacidade_maxima:
                    classe_item = item_a_ser_adicionado.__class__
                    novo_item = classe_item(nome=item_a_ser_adicionado.nome, preco= item_a_ser_adicionado.preco,quantidade=item_a_ser_adicionado.quantidade)
                    for item in self.itens:
                        if item is None:
                            indice_novo_item = self.itens.index(item)
                            self.itens[indice_novo_item] = novo_item
                            break
            elif self.capacidade_atual < self.capacidade_maxima:
                classe_item = item_a_ser_adicionado.__class__
                novo_item = classe_item()
                for item in self.itens:
                    if item is None:
                        indice_novo_item = self.itens.index(item)
                        self.itens[indice_novo_item] = novo_item
                        break
                
    def remover_item(self, item):
        if item in self.__itens:  
            if isinstance(item, ItemQuantizavel):
                item.reduz_quantidade(1)
                if item.quantidade == 0:
                    self.__itens.remove(item)
                    self.__itens.append(None)
                return
            if isinstance(item, Item):             
                    self.__itens.remove(item)
                    self.__itens.append(None)
                    return
