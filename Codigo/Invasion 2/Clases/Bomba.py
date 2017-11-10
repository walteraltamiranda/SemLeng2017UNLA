import pygame
import random

class Bomba(pygame.sprite.Sprite):
    def __init__(self,posX,posY):
        pygame.sprite.Sprite.__init__(self)
        
        self.imagenDisparo = pygame.image.load("Imagenes/bomba.jpg")
        
        self.rect = self.imagenDisparo.get_rect()
        
        self.velocidadDisparo =5
        
        self.rect.top = posY
        self.rect.left = posX
        
    def recorrido(self):
        self.rect.top = self.rect.top - self.velocidadDisparo   
         
    def dibujar(self, superficie):
        superficie.blit(self.imagenDisparo, self.rect)