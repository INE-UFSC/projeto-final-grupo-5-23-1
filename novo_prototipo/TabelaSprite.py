import pygame

class TabelaSprite():
	def __init__(self, imagem):
		self.__tabela = imagem

	@property
	def tabela(self):
		return self.__tabela
	
	@tabela.setter
	def tabela(self, imagem):
		self.__tabela = imagem

	def get_frame(self, animacao: int, frame: int, comprimento: int, altura: int, escala: int, cor: str):
		imagem = pygame.Surface((comprimento, altura)).convert_alpha()
		imagem.blit(self.tabela, (0, 0), ((frame * comprimento), (animacao * altura), comprimento, altura))
		imagem = pygame.transform.scale(imagem, (comprimento * escala, altura * escala))
		imagem.set_colorkey(cor)
		return imagem