class Auto():
	gasolina = 0
	# Metodo Constructor
   	def __init__(self, gasolina):
		Auto.gasolina = gasolina
        print "Tenemos", gasolina, "litros"
	
	@classmethod
	def arrancar(cls, gasolina):
		if gasolina > 0:
			print "Arranca"
		else:
			print "No Arranca"
		
	@classmethod
	def conducir(cls, gasolina):
		if gasolina > 0:
			gasolina -= 1
			print "Quedan", gasolina, "litros"
		else:
			print "No se mueve..."

# Clase Helicoptero hereda de Auto
class Helicoptero(Auto):
	pass
"""mi_auto = Auto(50)
### cuanta gasolina tenemos
print mi_auto.gasolina
# arrancamos el carro
mi_auto.arrancar()
mi_auto.conducir()
mi_auto.conducir()
mi_auto.conducir()
mi_auto.conducir()"""
