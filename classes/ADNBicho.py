class ADNBicho:
	"""A simple example class"""
	__vida = 0
	__satisfecho = 0
	__descansado = 0
	__entretencion = 0
	__nivel = 0
	__multiplicador = 0

	def __init__(self):
		__vida = 3

	def __setVida(self):
		print "holis"
		# return True

	# def __setSatisfecho():
	# 	return True

	# def __setDescansado():
	# 	return True

	# def __setEntretencion():
	# 	return True

	# def __setNivel():
	# 	return True

	# def __setMultiplicador():
	# 	return True

	def getVida(self):
		print "holis"
		# return True

	# def isVivo():
	# 	return True

	# def tomarPosicion():
	# 	return True

	# def vivir():
	# 	return True

	# def comer():
	# 	return True

	# def dormir():
	# 	return True

	# def jugar():
	# 	return True


class Bicho(ADNBicho):
	text = "asda"

	def __init__(self):
		ADNBicho.__init__(self)

	def holis(self):
		print "holahola"
		ADNBicho.getVida(self)


uno = Bicho()
uno.holis()