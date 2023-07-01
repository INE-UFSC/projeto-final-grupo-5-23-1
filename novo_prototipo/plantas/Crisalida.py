import pygame
from itens.recursos.Criofru import Criofru
from itens.Item import Item
from plantas.interfaces.IPlanta import IPlanta
import os


dir_atual = os.path.dirname(os.path.abspath(__file__))
pasta_assets = os.path.join(dir_atual, '..', 'assets', 'ui')
caminho_broto = os.path.join(pasta_assets, 'broto_azul.png')
caminho_muda = os.path.join(pasta_assets, 'muda_azul.png')
caminho_planta = os.path.join(pasta_assets, 'planta_azul.png')

class Crisalida(IPlanta):

    def __init__(self, pos, grupo):
        super().__init__(nome='Crisalida', pos=pos, grupo=grupo)
        self.__imagem_broto = pygame.transform.scale(pygame.image.load(caminho_broto), (200, 200))
        self.__imagem_muda = pygame.transform.scale(pygame.image.load(caminho_muda), (200, 200))
        self.__imagem_planta = pygame.transform.scale(pygame.image.load(caminho_planta), (250, 250))
        self.__imagem_atual = self.__imagem_broto
        self.__rect = self.image.get_rect(midbottom=pos)
        
        #--------------------------------------------------------
         # Tempo de crescimento dos estágios
        self.temposBase = [12.0, 32.0]
        self.temposRegada = [9.0, 24.0]

        self.temposAtuais = self.temposBase
        #--------------------------------------------------------
        
    @property
    def image(self):
        return self.__imagem_atual
    
    @image.setter
    def image(self, nova_imagem):
        self.__imagem_atual = nova_imagem

    @property
    def rect(self):
        return self.__rect
    
    def atualiza_sprite(self):
        posicao_antiga = self.__rect.midbottom
        self.agora = pygame.time.get_ticks()
        segundos = self.calcular_segundos()

        if segundos < self.temposAtuais[0]:
            self.image = self.__imagem_broto
            
        elif self.temposAtuais[0] < segundos < self.temposAtuais[1]:
            self.image = self.__imagem_muda

        elif segundos >= self.temposAtuais[1]:
            self.image = self.__imagem_planta
            self.em_crescimento = False
        
        self.__rect = self.image.get_rect(midbottom = posicao_antiga)


    def interagir(self, jogador):
        if not self.em_crescimento:
            lista_nomes_itens = []
            for item in jogador.inventario.itens:
                if isinstance(item, Item):
                    lista_nomes_itens.append(item.nome)
            item = Criofru()
            if (jogador.inventario.capacidade_atual < jogador.inventario.capacidade_maxima) or (item.nome in  lista_nomes_itens):
                jogador.inventario.adicionar_item(item)
                self.notifica_exclui_planta()

    def multiplicador_clima(self):
        if self.clima == 'Floresta':
            multiplicador = 1.5
        elif self.clima == 'Deserto':
            multiplicador = 3
        elif self.clima == 'Caverna':
            multiplicador = 1.8
        elif self.clima == 'Neve':
            multiplicador = 1
        elif self.clima == 'Planicie':
            multiplicador = 2
        else:
            multiplicador = 1
        return multiplicador