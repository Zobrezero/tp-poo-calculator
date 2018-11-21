import pilasengine

pilas = pilasengine.iniciar()

class ADNBicho(object):
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

	def iniciar(self):
		self.imagen = "Agregar.png"

	def holis(self):
		print("hola3")

uno = Bicho(pilas)

# llama al método heredado del actor
uno.decir(u"holis!")

# llama al método heredado del ADNBicho
uno.getVida()

# llama al método propio de Bicho
uno.holis()

pilas.ejecutar()