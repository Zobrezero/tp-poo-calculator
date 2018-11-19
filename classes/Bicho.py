from ADNBicho import ADNBicho
from assets import pilasengine
from assets import pilas

class Bicho(ADNBicho, pilasengine.actores.Actor):
	text = "asda"

	def __init__(self):
		ADNBicho.__init__(self)

	def holis(self):
		print "holahola"
		ADNBicho.getVida(self)



uno = Bicho()
uno.holis()
uno.decir("holisisisi")