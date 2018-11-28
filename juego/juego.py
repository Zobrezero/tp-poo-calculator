import pilasengine
import random

pilas = pilasengine.iniciar()

class ADNBicho(object):
	__vida = 100

	__descansado   = 50
	__entretencion = 50
	__satisfecho   = 50

	__aumento_vida = 25
	__descenso_vida = 0

	__nivel = 0

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

	def setDescensoVida(self, vid):
		self.__descenso_vida = vid

	def setAumentoVida(self, vid):
		self.__aumento_vida = vid

	def vivir(self):
		self.__vida = self.__vida - self.__descenso_vida
		return True if self.__vida > 0  else False

	def aumentarVida(self):
		self.__vida = self.__vida + self.__aumento_vida

	def getVida(self):
		return self.__vida

	def isVivo(self):
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
		return ADNBicho.vivir(self)

	def iniciar(self):
		self.setDescensoVida(7)
		self.setDescensoVida(10)
		self.imagen = "Bicho1.png"
		self.__barra = pilas.actores.Energia(self.getVida() , ancho=90, alto=10)
		self.set_cuando_hace_click(self.meTocaron)

	def posicionarBarra(self):
		self.__barra.x = self.x
		self.__barra.y = self.y - 50

	def matar(self):
		self.__barra.eliminar()
		self.eliminar()

	def meTocaron(self):
		self.aumentarVida()

class BichoVerde(pilasengine.actores.Actor, ADNBicho):
	def vivir(self):
		self.__barra.progreso = self.getVida()
		return ADNBicho.vivir(self)

	def iniciar(self):
		self.setDescensoVida(1)
		self.setDescensoVida(2)
		self.imagen = "Bicho2.png"
		self.__barra = pilas.actores.Energia(self.getVida() , ancho=90, alto=10)
		self.set_cuando_hace_click(self.meTocaron)

	def posicionarBarra(self):
		self.__barra.x = self.x
		self.__barra.y = self.y - 50

	def matar(self):
		self.__barra.eliminar()
		self.eliminar()

	def meTocaron(self):
		self.aumentarVida()

class BichoAzul(pilasengine.actores.Actor, ADNBicho):
	def vivir(self):
		self.__barra.progreso = self.getVida()
		return ADNBicho.vivir(self)

	def iniciar(self):
		self.setDescensoVida(3)
		self.setDescensoVida(5)
		self.imagen = "Bicho3.png"
		self.__barra = pilas.actores.Energia(self.getVida() , ancho=90, alto=10)
		self.set_cuando_hace_click(self.meTocaron)

	def posicionarBarra(self):
		self.__barra.x = self.x
		self.__barra.y = self.y - 50

	def matar(self):
		self.__barra.eliminar()
		self.eliminar()

	def meTocaron(self):
		self.aumentarVida()

bichos = []

btnStart   = pilas.interfaz.Boton(texto="Empezar el juego")
btnStart.x = 240
btnStart.y = -230

lastPositionX = -275
lastPositionY = 200


def loopMatarBichos():
	global lastPositionX
	global lastPositionY
	lastPositionX = -275
	lastPositionY = 200
	if (len(bichos)):
		for i in range(len(bichos)):
			aux2 = bichos[i]
			aux2.matar()

def finDelJuego():
	pilas.tareas.eliminar_todas()
	loopMatarBichos()
	pilas.avisar("Fin del juego!")
	btnStart.activar()

def restarPosicion():
	global lastPositionX
	global lastPositionY
	lastPositionX = lastPositionX + 100
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
			aux2.vivir()
			if (aux2.vivir() != True):
				finDelJuego()

def incrementarDificultad():
	generarBicho()
	generarBicho()
	generarBicho()

def empezarJuego():
	btnStart.desactivar()
	incrementarDificultad()
	pilas.tareas.siempre(0.5, loopControl) 
	pilas.tareas.siempre(20, incrementarDificultad) 

btnStart.conectar(empezarJuego)

pilas.ejecutar()