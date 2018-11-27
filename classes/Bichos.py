from ADNBicho import ADNBicho
# from assets import pilasengine
# from assets import pilas
import pilasengine

pilas = pilasengine.iniciar()

class BichoRojo(pilasengine.actores.Actor, ADNBicho):
	def iniciar(self):
		self.imagen = "classes/rojo.png"

	def comer(self):
		self.__setVida(__suma_vida * __multiplicador_vida)

class BichoVerde(pilasengine.actores.Actor, ADNBicho):
	__suma_vida = 20
	def iniciar(self):
		self.imagen = "classes/verde.png"


class BichoAzul(pilasengine.actores.Actor, ADNBicho):
	def iniciar(self):
		self.imagen = "classes/azul.png"