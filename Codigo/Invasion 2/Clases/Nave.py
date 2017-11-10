import pygame
import random
import Clases.Disparo as disp
import Clases.Bomba as bomb

class Nave(pygame.sprite.Sprite):
	"""docstring for Nave"""
	def __init__(self,imagenA, imagenB, ancho,alto):
		pygame.sprite.Sprite.__init__(self)
		self.ImagenNave = imagenA
		self.ImagenNaveB = imagenB
		self.rect = self.ImagenNave.get_rect()
		self.rect.centerx = ancho/2
		self.rect.centery = alto -80
		self.listaDisparo = []
		self.listaDisparoBomba = []
		self.cant_colisiones = 200
		self.cantBombas = 20

	def disparar(self,x,y):
		miDisparo = disp.Disparo(x,y)
		self.listaDisparo.append(miDisparo)

	def dispararBomba(self,x,y):
		miDisparoBomba = bomb.Bomba(x,y)
		if self.cantBombas > 0:
			self.listaDisparoBomba.append(miDisparoBomba)

	def dibujar(self, superficie):
		superficie.blit(self.ImagenNave, self.rect)
	
	def movimiento(self):
		if self.rect.left <= 0:
			self.rect.left = 0
		if self.rect.right > 1024:
			self.rect.right = 1024