from ADNBicho import ADNBicho

class Bicho(ADNBicho):
	text = "asda"

	def __init__(self):
		ADNBicho.__init__(self)

	def holis(self):
		print "holahola"
		ADNBicho.getVida(self)


uno = Bicho()
uno.holis()