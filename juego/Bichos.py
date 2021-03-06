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
		__vida = 3

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
		self.imagen = "rojo.png"

	def vivir(self):
		return True #if self.__vida > 0  else False

	def saludar(self):
		print("Hola wachin")

class BichoVerde(pilasengine.actores.Actor, ADNBicho):
	#def __init__(self):
	#	ADNBicho.__init__()

	def iniciar(self):
		self.imagen = "verde.png"

	def vivir(self):
		return True #if self.__vida > 0  else False

	def saludar(self):
		print("Hola wachin")

class BichoAzul(pilasengine.actores.Actor, ADNBicho):
	#def __init__(self):
	#	ADNBicho.__init__()

	def iniciar(self):
		self.imagen = "azul.png"

	def vivir(self):
		return True #if self.__vida > 0  else False

	def saludar(self):
		print("Hola wachin")

