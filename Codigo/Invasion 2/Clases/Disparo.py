import pygame
import random

class Disparo(pygame.sprite.Sprite):
    def __init__(self,posX,posY):
        pygame.sprite.Sprite.__init__(self)
        
        self.imagenDisparo = pygame.image.load("Imagenes/disparo.jpg")
        
        self.rect = self.imagenDisparo.get_rect()
        
        self.velocidadDisparo =3
        
        self.rect.top = posY
        self.rect.left = posX
        self.speed = [3,3]
        
    def recorrido(self):
        self.rect.top = self.rect.top - self.velocidadDisparo   
         
    def dibujar(self, superficie):
        superficie.blit(self.imagenDisparo, self.rect)