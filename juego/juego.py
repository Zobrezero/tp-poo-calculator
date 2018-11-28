import pilasengine
#from   Bichos import *
import random

# Global vars
pilas = pilasengine.iniciar()


import pilasengine

class ADNBicho(object):
	__vida = 100

	__descansado   = 50
	__entretencion = 50
	__satisfecho   = 50

	__suma_vida = 25

	__multiplicador_vida         = 1
	__multiplicador_descansado   = 1
	__multiplicador_entretencion = 1
	__multiplicador_satisfecho   = 1

	__nivel = 0

	def __init__(self):
		self.__vida = 0

	def __setVida(self, vida):
		self.__vida = self.vida + vida

	def __setSatisfecho(self):
		return None

	def __setDescansado(self):
		return None

	def __setEntretencion(self):
		return None

	def __setNivel(self):
		return None

	def __setMultiplicador(self):
		return None

	def vivir(self):
		return True if self.__vida > 0  else False

	def getVida(self):
		return self.__vida

	def isVivo(self):
		return None

	def tomarPosicion(self):
		return None

	def comer(self):
		return None

	def dormir(self):
		return None

	def jugar(self):
		return None

class BichoRojo(pilasengine.actores.Actor, ADNBicho):
	def vivir(self):
		self.__barra.progreso = self.getVida()

	def iniciar(self):
		self.imagen = "Bicho1.png"
		self.__barra = pilas.actores.Energia(self.getVida() , ancho=90, alto=10)

	def posicionarBarra(self):
		self.__barra.x = self.x
		self.__barra.y = self.y - 50

	def saludar(self):
		print("Hola wachin")

class BichoVerde(pilasengine.actores.Actor, ADNBicho):
	def vivir(self):
		self.__barra.progreso = self.getVida()

	def iniciar(self):
		self.imagen = "Bicho2.png"
		self.__barra = pilas.actores.Energia(self.getVida() , ancho=90, alto=10)

	def posicionarBarra(self):
		self.__barra.x = self.x
		self.__barra.y = self.y - 50

	def saludar(self):
		print("Hola wachin")

class BichoAzul(pilasengine.actores.Actor, ADNBicho):
	def vivir(self):
		self.__barra.progreso = self.getVida()

	def iniciar(self):
		self.imagen = "Bicho3.png"
		self.__barra = pilas.actores.Energia(self.getVida() , ancho=90, alto=10)

	def posicionarBarra(self):
		self.__barra.x = self.x
		self.__barra.y = self.y - 50

	def saludar(self):
		print("Hola wachin")

bichos = []

btnStart   = pilas.interfaz.Boton(texto="Empezar el juego")
btnStart.x = -240
btnStart.y = -230

lastPositionX = -275
lastPositionY = 200

def finDelJuego():
	pilas.tareas.eliminar_todas()

def restarPosicion():
	global lastPositionX
	global lastPositionY
	lastPositionX = lastPositionX + 100
	#lastPositionY = lastPositionY - 50
	if (len(bichos) % 6 == 0):
		lastPositionY = lastPositionY -100
		lastPositionX = -285

def bichoRandom():
	r = random.randint(1,3)
	if (r == 1):
		return BichoVerde(pilas)
	elif (r == 2):
		return BichoRojo(pilas)
	elif (r == 3):
		return BichoAzul(pilas)

def generarBicho():
	aux = bichoRandom()
	aux.x = lastPositionX
	aux.y = lastPositionY
	aux.posicionarBarra()
	bichos.append(aux)
	restarPosicion()

def loopControl():
	if (len(bichos)):
		for i in range(len(bichos)):
			aux2 = bichos[i]
			if (aux2.vivir() != True):
				finDelJuego()

def incrementarDificultad():
	generarBicho()
	generarBicho()
	generarBicho()

def empezarJuego():
	incrementarDificultad()
	pilas.tareas.siempre(1, loopControl) 
	pilas.tareas.siempre(5, incrementarDificultad) 

btnStart.conectar(empezarJuego)
pilas.ejecutar()