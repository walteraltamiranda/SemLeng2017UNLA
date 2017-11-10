import pygame
import random
import os
import time


#Creo algunos variables fijas
NEGRO = ( 0, 0, 0 )
WHITE = (255, 255, 255)
alto = 768
ancho = 1024


class Nave(pygame.sprite.Sprite):
	"""docstring for Nave"""
	def __init__(self,imagenA, imagenB):
		pygame.sprite.Sprite.__init__(self)
		self.ImagenNave = imagenA
		self.ImagenNaveB = imagenB
		self.rect = self.ImagenNave.get_rect()
		self.rect.centerx = ancho/2
		self.rect.centery = alto -75
		self.listaDisparo = []
		self.listaDisparoBomba = []
		self.cant_colisiones = 200

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
        
        self.velocidadDisparo =3
        
        self.rect.top = posY
        self.rect.left = posX
        self.speed = [3,3]
        
    def recorrido(self):
        self.rect.top = self.rect.top - self.velocidadDisparo   
         
    def dibujar(self, superficie):
        superficie.blit(self.imageDisparo, self.rect)
    
class DisparoEnemigo(pygame.sprite.Sprite):
    def __init__(self,posX,posY):
        pygame.sprite.Sprite.__init__(self)
        
        self.imageDisparo = pygame.image.load("Imagenes/disparo.jpg")
        
        self.rect = self.imageDisparo.get_rect()
        
        self.velocidadDisparo =6
        
        self.rect.bottom = posY
        self.rect.left = posX
        self.speed = [3,3]
        
    def recorrido(self):
        self.rect.bottom = self.rect.bottom + self.velocidadDisparo   
         
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
        self.imagenEnemigoA = pygame.image.load("Imagenes/enem_cortado01.PNG").convert_alpha()
        self.imagenEnemigoB = pygame.image.load("Imagenes/enem_cortado02.PNG").convert_alpha()
        self.listaImagen = [self.imagenEnemigoA, self.imagenEnemigoB]
        self.posImagen = 0
        self.imagenEnemigo = self.listaImagen[self.posImagen]
        self.rect = self.imagenEnemigo.get_rect()
        self.rect.centerx = random.randrange(100,900)
        self.rect.centery = random.randrange(100,500)
        self.Vida = True
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
        if self.rect.left < 0 or self.rect.right > ancho:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > 568:
            self.speed[1] = -self.speed[1]
        self.rect.move_ip((self.speed[0], self.speed[1]))

    def disparar(self,x,y):
    	miDisparo = DisparoEnemigo(x,y)
    	self.listaDisparo.append(miDisparo)

class Boss(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagenEnemigoA = pygame.image.load("Imagenes/boss_corte01.PNG").convert_alpha()
        self.imagenEnemigoB = pygame.image.load("Imagenes/boss_corte02.PNG").convert_alpha()
        self.listaImagen = [self.imagenEnemigoA, self.imagenEnemigoB]
        self.posImagen = 0
        self.imagenEnemigo = self.listaImagen[self.posImagen]
        self.rect = self.imagenEnemigo.get_rect()
        self.rect.centerx = random.randrange(100,900)
        self.rect.centery = random.randrange(100,500)
        self.Vida = True
        self.speed = [6,6]
        self.tiempoCambio = 1
        self.cant_colisiones = 200
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
        if self.rect.left < 0 or self.rect.right > ancho:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > 768:
            self.speed[1] = -self.speed[1]
        self.rect.move_ip((self.speed[0], self.speed[1]))
		
def menu_inicio():
	os.environ['SDL_VIDEO_CENTERED'] = '1'
	pygame.init()	#Inicializo el motor del juego
	pygame.mixer.init() # Inicializo el motor de sonidos
	dimensiones = (ancho,alto) #Defino el tamaño de la pantalla
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
	pygame.mixer.music.load("Sonidos/soundtrack.mp3")
	pygame.mixer.music.play()


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
					cargar_partida()
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
	imagen_fondo = pygame.image.load("Imagenes/ideamenucreditos.JPG").convert()
	
	while not fin:
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				fin = True
			elif evento.type == pygame.KEYDOWN:
				if evento.key == pygame.K_ESCAPE:
					return 0
		pantalla.blit(imagen_fondo,[0,0])
		
		pygame.display.flip()
		reloj.tick(60)

	pygame.quit()

def cargar_partida():
	dimensiones = (ancho,alto)
	pantalla = pygame.display.set_mode(dimensiones)
	pygame.display.set_caption("Invasión")
	fin = False
	reloj = pygame.time.Clock()
	imagen_fondo = pygame.image.load("Imagenes/ideagraficoproximamente.JPG").convert()
	
	while not fin:
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				fin = True
			elif evento.type == pygame.KEYDOWN:
				if evento.key == pygame.K_ESCAPE:
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
	imagenNave1A = pygame.image.load("Imagenes/nave1-1_corte.PNG").convert_alpha()
	imagenNave1B = pygame.image.load("Imagenes/nave1-2.PNG").convert_alpha()
	imagenNave2A = pygame.image.load("Imagenes/nave2-1.png").convert_alpha()
	imagenNave2B = pygame.image.load("Imagenes/nave2-2.png").convert_alpha()
	
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
					main(imagenNave1A,imagenNave1B)
				elif 570 <= x_mouse <= 734 and 413 <= y_mouse <= 511:
					main(imagenNave2A,imagenNave2B)
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
	imagen_volver = pygame.image.load("Imagenes/volveratras.PNG").convert_alpha()				
	while not fin:
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				fin = True
			elif evento.type == pygame.KEYDOWN:
				if evento.key == pygame.K_ESCAPE:
					return 0
		
		pantalla.blit(imagen_pausa,[270,250])
		pantalla.blit(imagen_volver,[290,600])

		pygame.display.flip()
		reloj.tick(60)

	pygame.quit()

def perdiste():
	dimensiones = (ancho,alto)
	pantalla = pygame.display.set_mode(dimensiones)
	pygame.display.set_caption("Invasión - Juego Perdido")
	fin = False
	reloj = pygame.time.Clock()
	pantalla.fill(NEGRO)	
	
	imagen_perdiste= pygame.image.load("Imagenes/perder.PNG").convert_alpha()
	imagen_continuar= pygame.image.load("Imagenes/continuar.PNG").convert_alpha()

	while not fin:
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				fin = True
			elif evento.type == pygame.KEYDOWN:
				if evento.key == pygame.K_s:
					selecciona_jugador()
		
		pantalla.blit(imagen_perdiste,[150,200])
		pantalla.blit(imagen_continuar,[150,650])
		
		pygame.display.flip()
		reloj.tick(60)

	pygame.quit()

def ganaste():
	dimensiones = (ancho,alto)
	pantalla = pygame.display.set_mode(dimensiones)
	pygame.display.set_caption("Invasión - Juego Perdido")
	fin = False
	reloj = pygame.time.Clock()
	pantalla.fill(NEGRO)	
	
	imagen_ganaste= pygame.image.load("Imagenes/ganar.PNG").convert_alpha()
	imagen_continuar= pygame.image.load("Imagenes/continuar.PNG").convert_alpha()
				
	while not fin:
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				fin = True
			elif evento.type == pygame.KEYDOWN:
				if evento.key == pygame.K_s:
					selecciona_jugador()
		
		pantalla.blit(imagen_ganaste,[150,200])
		pantalla.blit(imagen_continuar,[150,650])		
		pygame.display.flip()
		reloj.tick(60)

	pygame.quit()

def main(a,b):
	dimensiones = (ancho,alto)

	pantalla = pygame.display.set_mode(dimensiones)

	pygame.display.set_caption("Invasión")
	#Variable de cierre
	fin = False
	Fuente = pygame.font.SysFont("Arial",30)
	#aux=1
	#aux2=50
	reloj = pygame.time.Clock()

	pygame.key.set_repeat(10, 50)  # Activa repeticion de teclas
	#Defino la biblioteca de sonidos
	sonido_disparo = pygame.mixer.Sound("Sonidos/Blip 003.WAV")
	sonido_disparoBomba = pygame.mixer.Sound("Sonidos/Blip 004.WAV")
	sonido_colision = pygame.mixer.Sound("Sonidos/Noise 002.WAV")
	sonido_boss = pygame.mixer.Sound("Sonidos/Phat Retro Bass 001.WAV")
	sonido_boss.set_volume(0.3)	

	#Defino las imagenes a cargar
	imagen_fondo = pygame.image.load("Imagenes/fondo_juego.JPG").convert()
	
	jugador_1 = Nave(a,b)
	disparo =Disparo(ancho/2, alto -50)
	disparoBomba =Bomba(ancho/2, alto -50)
	disparoEnemigo = DisparoEnemigo(ancho/2, alto-700)

	listaEnemigo = [] 
	for i in range(50):
		listaEnemigo.append(Enemigo())

	boss = Boss()
		
	while not fin:
		reloj.tick(60)

		jugador_1.movimiento()
		disparo.recorrido()
		disparoBomba.recorrido()
		disparoEnemigo.recorrido()
		Tiempo = int(pygame.time.get_ticks()/1000)
		
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
			obj.comportamiento(Tiempo)
			
			if Tiempo % 5 ==0:
				x,y=obj.rect.center
				obj.disparar(x,y)

			if len(obj.listaDisparo)>0:
				for x in obj.listaDisparo:
					x.dibujar(pantalla)
					x.recorrido()

				if x.rect.colliderect(jugador_1.rect):
					jugador_1.cant_colisiones-=1
			for y in jugador_1.listaDisparo:
				if obj.rect.colliderect(y.rect):
					sonido_colision.play()
					if obj in listaEnemigo:
						listaEnemigo.remove(obj)
					if y in jugador_1.listaDisparo:
						jugador_1.listaDisparo.remove(y)
					
		


		if len(jugador_1.listaDisparo)>0:
			for x in jugador_1.listaDisparo:
				x.dibujar(pantalla)
				x.recorrido()

				if x.rect.top < 50:
					jugador_1.listaDisparo.remove(x)

		if len(jugador_1.listaDisparoBomba)>0:
			for x in jugador_1.listaDisparoBomba:
				x.dibujar(pantalla)
				x.recorrido()
				for obj in listaEnemigo:
					if x.rect.colliderect(obj.rect):
						listaEnemigo.remove(obj) 

				if x.rect.top < 50:
					jugador_1.listaDisparoBomba.remove(x)
		
		if len(listaEnemigo) == 0:
			
			sonido_boss.play()
						
			boss.dibujar(pantalla)
			boss.update()
			boss.comportamiento(Tiempo)

			if jugador_1.rect.colliderect(boss.rect):
				jugador_1.cant_colisiones-=1
				
				#if jugador_1.cant_colisiones == 0:
				#	perdiste()

			for y in jugador_1.listaDisparo:
				if boss.rect.colliderect(y.rect):
					boss.cant_colisiones-=1
					jugador_1.listaDisparo.remove(y)
					
					if boss.cant_colisiones <= 0:
						ganaste()
						
			for z in jugador_1.listaDisparoBomba:
				if boss.rect.colliderect(z.rect):
					boss.cant_colisiones-=5
					jugador_1.listaDisparoBomba.remove(z)
					
					if boss.cant_colisiones <= 0:
						ganaste()

		if jugador_1.cant_colisiones ==0:
			perdiste()				

		contador = Fuente.render('VIDA JUGADOR: '+str(jugador_1.cant_colisiones),0,(255,0,255))
		contador2 = Fuente.render('VIDA ENEMIGO: ' +str(boss.cant_colisiones),0,(255,0,255))
		pantalla.blit(contador,(780,728))
		pantalla.blit(contador2,(780,10))
		pygame.display.flip()



	pygame.quit()

menu_inicio()