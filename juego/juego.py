import pilasengine
from Bichos import *
import random

# Global vars
pilas = pilasengine.iniciar()

bichos = []

btnStart   = pilas.interfaz.Boton(texto="Empezar el juego")
btnStart.x = -240
btnStart.y = -230

lastPositionX = -250
lastPositionY = 250


def restarPosicion():
	global lastPositionX
	global lastPositionY
	lastPositionX = lastPositionX + 50
	lastPositionY = lastPositionY - 50

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
	restarPosicion()

def loopControl():
	if (len(bichos)):
		for i in range(len(bichos)):
			bichos[i].vivir()

def incrementarDificultad():
	generarBicho()
	generarBicho()
	generarBicho()

def empezarJuego():
	incrementarDificultad()
	pilas.tareas.siempre(1, loopControl) 
	pilas.tareas.siempre(30, incrementarDificultad) 


btnStart.conectar(empezarJuego)
pilas.ejecutar()