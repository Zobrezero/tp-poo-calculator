
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

	def vivir(self):
		return None

	def comer(self):
		return None

	def dormir(self):
		return None

	def jugar(self):
		return None

class BichoRojo(pilasengine.actores.Actor, ADNBicho):
	def iniciar(self):
		self.imagen = "rojo.png"

	def comer(self):
		self.__setVida(__suma_vida * __multiplicador_vida)

class BichoVerde(pilasengine.actores.Actor, ADNBicho):
	__suma_vida = 20
	def iniciar(self):
		self.imagen = "verde.png"


class BichoAzul(pilasengine.actores.Actor, ADNBicho):
	def iniciar(self):
		self.imagen = "azul.png"
