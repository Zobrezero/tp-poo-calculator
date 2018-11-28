import pilasengine
#from   Bichos import *
import random

# Global vars
pilas = pilasengine.iniciar()


import pilasengine

class ADNBicho(object):
	__vida = 1000

	__descansado   = 50
	__entretencion = 50
	__satisfecho   = 50

	__suma_vida = 25
	__descenso_vida = 0

	__multiplicador_vida         = 1
	__multiplicador_descansado   = 1
	__multiplicador_entretencion = 1
	__multiplicador_satisfecho   = 1

	__nivel = 0

	def __init__(self):
		__vida = 10000

	def setVida(self,vid):
		self.__descenso_vida = vid

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
		print (self.__descenso_vida)
		self.__vida = self.__vida - self.__descenso_vida
		return True if self.__vida > 0  else False

	def getVida(self):
		return None

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
	#def __init__(self):
	#	ADNBicho.__init__()
	

	def iniciar(self):
		self.setVida(22)
		self.imagen = "rojo.png"

	def saludar(self):
		print("Hola wachin")

class BichoVerde(pilasengine.actores.Actor, ADNBicho):
	#def __init__(self):
	#	ADNBicho.__init__()
	

	def iniciar(self):
		self.setVida(16)
		self.imagen = "verde.png"

	def saludar(self):
		print("Hola wachin")

class BichoAzul(pilasengine.actores.Actor, ADNBicho):
	#def __init__(self):
	#	ADNBicho.__init__()
	

	def iniciar(self):
		self.imagen = "azul.png"
		self.setVida(12)

	def saludar(self):
		print("Hola wachin")




bichos = []

btnStart   = pilas.interfaz.Boton(texto="Empezar el juego")
btnStart.x = -240
btnStart.y = -230

lastPositionX = -275
lastPositionY = 200

def finDelJuego():
	print("fin del juego")
	pilas.tareas.eliminar_todas()

def restarPosicion():
	global lastPositionX
	global lastPositionY
	lastPositionX = lastPositionX + 100
	#lastPositionY = lastPositionY - 50

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
	bichos.append(aux)
	pilas.avisar("Hola, esto es un mensaje.")
	restarPosicion()

def loopControl():
	if (len(bichos)):
		for i in range(len(bichos)):
			aux2 = bichos[i]
			aux2.vivir()
			if (aux2.vivir() != True):
				finDelJuego()

def incrementarDificultad():
	generarBicho()
	generarBicho()
	generarBicho()

def empezarJuego():
	incrementarDificultad()
	pilas.tareas.siempre(1, loopControl) 
	pilas.tareas.siempre(10, incrementarDificultad) 

btnStart.conectar(empezarJuego)
pilas.ejecutar()