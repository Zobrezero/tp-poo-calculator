import pilasengine
#import Bicho

pilas = pilasengine.iniciar()

class ADNBicho:
	__vida = 0
	__satisfecho = 0
	__descansado = 0
	__entretencion = 0
	__nivel = 0
	__multiplicador = 0

	def __init__(self):
		__vida = 3

	def __setVida(self):
		print("holis1")

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

	def getVida(self):
		print("holis2")

	def isVivo(self):
		return None

	def tomarPosicion(self):
		return None

	def vivir(self):
		return None

	def comer(self):
		return None

	def dormir(self):
		return None

	def jugar(self):
		return None


class Bicho(pilasengine.actores.Actor, ADNBicho):
	text = "asda"

	def __init__(self):
		ADNBicho.__init__(self)

	def iniciar(self):
		self.imagen = "Agregar.png"

	def holis(self):
		print("hola3")
		ADNBicho.getVida(self)


#uno = Bicho()
#uno.holis()
#uno.decir("holisisisi")


class Alien(pilasengine.actores.Actor):
	


pilas.ejecutar()