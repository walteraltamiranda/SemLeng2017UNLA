import pygame
import random

class DisparoEnemigo(pygame.sprite.Sprite):
    def __init__(self,posX,posY):
        pygame.sprite.Sprite.__init__(self)
        
        self.imagenDisparo = pygame.image.load("Imagenes/disparo.jpg")
        
        self.rect = self.imagenDisparo.get_rect()
        
        self.velocidadDisparo =6
        
        self.rect.bottom = posY
        self.rect.left = posX
        self.speed = [3,3]
        
    def recorrido(self):
        self.rect.bottom = self.rect.bottom + self.velocidadDisparo   
         
    def dibujar(self, superficie):
        superficie.blit(self.imagenDisparo, self.rect)