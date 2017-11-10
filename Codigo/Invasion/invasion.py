import pygame
import random
import os

#Creo algunos colores
NEGRO = ( 0, 0, 0 )
WHITE = (255, 255, 255)
alto = 768
ancho = 1024

#Creo botones




#Clase de nave
class Nave(pygame.sprite.Sprite):
	"""docstring for Nave"""
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.ImagenNave = pygame.image.load("Imagenes/nave1-1.png").convert_alpha()
		self.rect = self.ImagenNave.get_rect()
		self.rect.centerx = ancho/2
		self.rect.centery = alto -125
		self.listaDisparo = []
		self.listaDisparoBomba = []
		self.Vida = True

	def disparar(self,x,y):
		miDisparo = Disparo(x,y)
		self.listaDisparo.append(miDisparo)

	def dispararBomba(self,x,y):
		miDisparoBomba = Bomba(x,y)
		self.listaDisparoBomba.append(miDisparoBomba)

	def dibujar(self, superficie):
		superficie.blit(self.ImagenNave, self.rect)
	
	def movimiento(self):
		if self.rect.left <= 0:
			self.rect.left = 0
		if self.rect.right > 1024:
			self.rect.right = 1024

class Nave2(pygame.sprite.Sprite):
	"""docstring for Nave"""
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.ImagenNave = pygame.image.load("Imagenes/nave2-1.png").convert_alpha()
		self.rect = self.ImagenNave.get_rect()
		self.rect.centerx = ancho/2
		self.rect.centery = alto -125
		self.listaDisparo = []
		self.listaDisparoBomba = []
		self.Vida = True

	def disparar(self,x,y):
		miDisparo = Disparo(x,y)
		self.listaDisparo.append(miDisparo)

	def dispararBomba(self,x,y):
		miDisparoBomba = Bomba(x,y)
		self.listaDisparoBomba.append(miDisparoBomba)

	def dibujar(self, superficie):
		superficie.blit(self.ImagenNave, self.rect)
	
	def movimiento(self):
		if self.rect.left <= 0:
			self.rect.left = 0
		if self.rect.right > 1024:
			self.rect.right = 1024

class Disparo(pygame.sprite.Sprite):
    def __init__(self,posX,posY):
        pygame.sprite.Sprite.__init__(self)
        
        self.imageDisparo = pygame.image.load("Imagenes/disparo.jpg")
        
        self.rect = self.imageDisparo.get_rect()
        
        self.velocidadDisparo =5
        
        self.rect.top = posY
        self.rect.left = posX
        
    def recorrido(self):
        self.rect.top = self.rect.top - self.velocidadDisparo   
         
    def dibujar(self, superficie):
        superficie.blit(self.imageDisparo, self.rect)

class Bomba(pygame.sprite.Sprite):
    def __init__(self,posX,posY):
        pygame.sprite.Sprite.__init__(self)
        
        self.imageDisparo = pygame.image.load("Imagenes/bomba.jpg")
        
        self.rect = self.imageDisparo.get_rect()
        
        self.velocidadDisparo =5
        
        self.rect.top = posY
        self.rect.left = posX
        
    def recorrido(self):
        self.rect.top = self.rect.top - self.velocidadDisparo   
         
    def dibujar(self, superficie):
        superficie.blit(self.imageDisparo, self.rect)

class Enemigo(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagenEnemigo = pygame.image.load("Imagenes/enem0.PNG").convert_alpha()
        self.rect = self.imagenEnemigo.get_rect()
        self.rect.centerx = random.randrange(100,900)
        self.rect.centery = random.randrange(100,500)
        self.Vida = True
        self.speed = [3,3]
    def dibujar(self, superficie):
    	superficie.blit(self.imagenEnemigo, self.rect)

    def update(self):
        if self.rect.left < 0 or self.rect.right > ancho:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > 668:
            self.speed[1] = -self.speed[1]
        self.rect.move_ip((self.speed[0], self.speed[1]))

    def colision(self, Enemigo):
    	if self.rect.colliderect(Enemigo.rect):
    		self.speed[0] = self.speed[0]


		
def menu_inicio():
	os.environ['SDL_VIDEO_CENTERED'] = '1'
	pygame.init()
	pygame.mixer.init()
	dimensiones = (ancho,alto)
	pantalla = pygame.display.set_mode(dimensiones)
	pygame.display.set_caption("Invasión")
	fin = False
	reloj = pygame.time.Clock()
	imagen_fondo = pygame.image.load("Imagenes/fondo.JPG").convert()
	imagen_iniciar = pygame.image.load("Imagenes/iniciar.PNG").convert_alpha()
	imagen_titulo = pygame.image.load("Imagenes/titulo.PNG").convert_alpha()
	imagen_cargar = pygame.image.load("Imagenes/cargar.PNG").convert_alpha()
	imagen_controles = pygame.image.load("Imagenes/controles.PNG").convert_alpha()
	imagen_creditos = pygame.image.load("Imagenes/creditos.PNG").convert_alpha()
	imagen_salir = pygame.image.load("Imagenes/salir.PNG").convert_alpha()
	sonido_seleccion = pygame.mixer.Sound("Sonidos/Engine Bass 001.WAV")



	while not fin:
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				fin = True
			
			elif evento.type == pygame.MOUSEBUTTONDOWN:
				x_mouse, y_mouse = pygame.mouse.get_pos()
				if 150 <= x_mouse <= 800 and 250 <= y_mouse <= 349:
					sonido_seleccion.play()
					selecciona_jugador()
				elif 155 <= x_mouse <= 800 and 350 <= y_mouse <= 449:
					cargar()
				elif 150 <= x_mouse <= 800 and 450 <= y_mouse <= 549:
					sonido_seleccion.play()
					controles()
				elif 310 <= x_mouse <= 698 and 550 <= y_mouse <= 649:
					sonido_seleccion.play()
					mostrar_creditos()	
				elif 150 <= x_mouse <= 800 and 650 <= y_mouse <= 749:
					sonido_seleccion.play()
					fin = True
					



		pantalla.blit(imagen_fondo,[0,0])
		pantalla.blit(imagen_titulo,[65,50])
		pantalla.blit(imagen_iniciar,[150,250])
		pantalla.blit(imagen_cargar,[155,350])
		pantalla.blit(imagen_controles,[150,450])
		pantalla.blit(imagen_creditos,[310,550])
		pantalla.blit(imagen_salir,[150,650])
		
			
	
	
		pygame.display.flip()
		reloj.tick(60)

	pygame.quit()

def controles():
	dimensiones = (ancho,alto)
	pantalla = pygame.display.set_mode(dimensiones)
	pygame.display.set_caption("Invasión")
	fin = False
	reloj = pygame.time.Clock()
	imagen_fondo = pygame.image.load("Imagenes/ideamenucontrol.JPG").convert()
	
	while not fin:
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				fin = True
			elif evento.type == pygame.KEYDOWN:
				if evento.key == pygame.K_x:
					return 0
		pantalla.blit(imagen_fondo,[0,0])

		pygame.display.flip()
		reloj.tick(60)

	pygame.quit()

def mostrar_creditos():
	dimensiones = (ancho,alto)
	pantalla = pygame.display.set_mode(dimensiones)
	pygame.display.set_caption("Invasión")
	fin = False
	reloj = pygame.time.Clock()
	imagen_fondo = pygame.image.load("Imagenes/ideamenucontrol.JPG").convert()
	
	while not fin:
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				fin = True
			elif evento.type == pygame.KEYDOWN:
				if evento.key == pygame.K_x:
					return 0
		pantalla.blit(imagen_fondo,[0,0])
		
		pygame.display.flip()
		reloj.tick(60)

	pygame.quit()

def selecciona_jugador():
	dimensiones = (ancho,alto)
	pantalla = pygame.display.set_mode(dimensiones)
	pygame.display.set_caption("Invasión")
	fin = False
	reloj = pygame.time.Clock()
	imagen_fondo = pygame.image.load("Imagenes/menuseleccion.JPG").convert()
	
	while not fin:
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				fin = True
			elif evento.type == pygame.KEYDOWN:
				if evento.key == pygame.K_x:
					return 0
			elif evento.type == pygame.MOUSEBUTTONDOWN:
				x_mouse, y_mouse = pygame.mouse.get_pos()
				print (y_mouse)
				if 296 <= x_mouse <= 494 and 395 <= y_mouse <= 535:
					main()
				elif 570 <= x_mouse <= 734 and 413 <= y_mouse <= 511:
					main2()
				
		pantalla.blit(imagen_fondo,[0,0])

		pygame.display.flip()
		reloj.tick(60)

	pygame.quit()

def pausa():
	dimensiones = (ancho,alto)
	pantalla = pygame.display.set_mode(dimensiones)
	pygame.display.set_caption("Invasión - Juego PAUSADO")
	fin = False
	reloj = pygame.time.Clock()
	pantalla.fill(NEGRO)	
	
	imagen_pausa = pygame.image.load("Imagenes/pausa.PNG").convert_alpha()				
	while not fin:
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				fin = True
			elif evento.type == pygame.KEYDOWN:
				if evento.key == pygame.K_ESCAPE:
					return 0
		
		pantalla.blit(imagen_pausa,[270,350])
		
		pygame.display.flip()
		reloj.tick(60)

	pygame.quit()

def main():
	dimensiones = (ancho,alto)

	pantalla = pygame.display.set_mode(dimensiones)

	pygame.display.set_caption("Invasión")
	#Variable de cierre
	fin = False
	
	
	reloj = pygame.time.Clock()
	pygame.key.set_repeat(10, 50)  # Activa repeticion de teclas
	#Defino la biblioteca de sonidos
	sonido_disparo = pygame.mixer.Sound("Sonidos/Blip 003.WAV")
	sonido_disparoBomba = pygame.mixer.Sound("Sonidos/Blip 004.WAV")
	pygame.mixer.music.load("Sonidos/WP.mp3")
	pygame.mixer.music.play()
	
	

	#Defino las imagenes a cargar
	imagen_fondo = pygame.image.load("Imagenes/fondo_juego.JPG").convert()
	
	jugador_1 = Nave()
	disparo =Disparo(ancho/2, alto -50)
	disparoBomba =Bomba(ancho/2, alto -50)

	listaEnemigo = [] 
	for i in range(50):
		listaEnemigo.append(Enemigo())
	

	while not fin:
		jugador_1.movimiento()
		disparo.recorrido()
		disparoBomba.recorrido()
		
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				fin = True
			elif evento.type == pygame.KEYDOWN:
				if evento.key == pygame.K_SPACE:
					x,y=jugador_1.rect.center
					jugador_1.disparar(x,y)
					sonido_disparo.play()
					disparo.dibujar(pantalla)
				elif evento.key == pygame.K_LCTRL:
					x2,y2 = jugador_1.rect.center
					jugador_1.dispararBomba(x2,y2)
					sonido_disparoBomba.play()
					disparoBomba.dibujar(pantalla)
				elif evento.key == pygame.K_ESCAPE:
					
					pausa()
				elif evento.key == pygame.K_RIGHT:
					jugador_1.rect.centerx += 20
				elif evento.key == pygame.K_LEFT:
					jugador_1.rect.centerx -= 20

		pantalla.blit(imagen_fondo,[0,0])
		jugador_1.dibujar(pantalla)
							
		for obj in listaEnemigo:
			obj.dibujar(pantalla)
			obj.update()
		
		   	
		if len(jugador_1.listaDisparo)>0:
			for x in jugador_1.listaDisparo:
				x.dibujar(pantalla)
				x.recorrido()
				if x.rect.top < 100:
					jugador_1.listaDisparo.remove(x)

		if len(jugador_1.listaDisparoBomba)>0:
			for x in jugador_1.listaDisparoBomba:
				x.dibujar(pantalla)
				x.recorrido()
				if x.rect.top < 100:
					jugador_1.listaDisparoBomba.remove(x)
	
		pygame.display.flip()
		reloj.tick(60)



	pygame.quit()

def main2():
	
	dimensiones = (ancho,alto)

	pantalla = pygame.display.set_mode(dimensiones)

	pygame.display.set_caption("Invasión")
	#Variable de cierre
	fin = False
	
	
	reloj = pygame.time.Clock()
	pygame.key.set_repeat(10, 50)  # Activa repeticion de teclas
	#Defino la biblioteca de sonidos
	sonido_disparo = pygame.mixer.Sound("Sonidos/Blip 003.WAV")
	sonido_disparoBomba = pygame.mixer.Sound("Sonidos/Blip 004.WAV")

	#Defino las imagenes a cargar
	imagen_fondo = pygame.image.load("Imagenes/fondo_juego.JPG").convert()
	
	jugador_2 = Nave2()
	disparo =Disparo(ancho/2, alto -50)
	disparoBomba =Bomba(ancho/2, alto -50)

	listaEnemigo = [] 
	for i in range(50):
		listaEnemigo.append(Enemigo())
	

	while not fin:
		jugador_2.movimiento()
		disparo.recorrido()
		disparoBomba.recorrido()
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				fin = True
			elif evento.type == pygame.KEYDOWN:
				if evento.key == pygame.K_SPACE:
					x,y=jugador_2.rect.center
					jugador_2.disparar(x,y)
					sonido_disparo.play()
					disparo.dibujar(pantalla)
				elif evento.key == pygame.K_LCTRL:
					x2,y2 = jugador_2.rect.center
					jugador_2.dispararBomba(x2,y2)
					sonido_disparoBomba.play()
					disparoBomba.dibujar(pantalla)
				elif evento.key == pygame.K_ESCAPE:
					pausa()
				elif evento.key == pygame.K_RIGHT:
					jugador_2.rect.centerx += 20
				elif evento.key == pygame.K_LEFT:
					jugador_2.rect.centerx -= 20

		pantalla.blit(imagen_fondo,[0,0])
		jugador_2.dibujar(pantalla)
				
		for obj in listaEnemigo:
			obj.dibujar(pantalla)
			obj.update()
		
		   	
		if len(jugador_2.listaDisparo)>0:
			for x in jugador_2.listaDisparo:
				x.dibujar(pantalla)
				x.recorrido()
				if x.rect.top < 100:
					jugador_2.listaDisparo.remove(x)

		if len(jugador_2.listaDisparoBomba)>0:
			for x in jugador_2.listaDisparoBomba:
				x.dibujar(pantalla)
				x.recorrido()
				if x.rect.top < 100:
					jugador_2.listaDisparoBomba.remove(x)
	
		pygame.display.flip()
		reloj.tick(60)



	pygame.quit()


menu_inicio()