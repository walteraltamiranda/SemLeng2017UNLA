import pygame
import random
import time
import Clases.DisparoEnemigo as dispE
class Enemigo(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagenEnemigoA = pygame.image.load("Imagenes/enem_cortado01.PNG").convert_alpha()
        self.imagenEnemigoB = pygame.image.load("Imagenes/enem_cortado02.PNG").convert_alpha()
        self.listaImagen = [self.imagenEnemigoA, self.imagenEnemigoB]
        self.posImagen = 0
        self.imagenEnemigo = self.listaImagen[self.posImagen]
        self.rect = self.imagenEnemigo.get_rect()
        self.rect.centerx = random.randrange(100,900)
        self.rect.centery = random.randrange(100,500)
        self.speed = [3,3]
        self.tiempoCambio = 1
        self.listaDisparo = []

    def comportamiento(self,tiempo):
    	if self.tiempoCambio == tiempo:
    		self.posImagen +=1
    		self.tiempoCambio+=1

    		if self.posImagen > len(self.listaImagen)-1:
    			self.posImagen=0
    def dibujar(self, superficie):
    	self.imagenEnemigo = self.listaImagen[self.posImagen]
    	superficie.blit(self.imagenEnemigo, self.rect)

    def update(self):
        if self.rect.left < 0 or self.rect.right > 1024:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > 568:
            self.speed[1] = -self.speed[1]
        self.rect.move_ip((self.speed[0], self.speed[1]))

    def disparar(self,x,y):
    	miDisparo = dispE.DisparoEnemigo(x,y)
    	self.listaDisparo.append(miDisparo)