class Clase(object):
	no_instanciada = 0

	def __init__(self):
		Clase.no_instanciada = Clase.no_instanciada + 1

	@classmethod
	def tomar_instancia(cls_obj):
		return cls_obj.no_instanciada
