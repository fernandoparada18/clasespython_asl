class Auto():
    gasolina = 0
    def __init__(self, gasolina):
        self.gasolina = gasolina
        print "Tenemos", gasolina, "litros"
		
	@staticnethod
	def arrancar(gasolina):
		if gasolina > 0:
			print "Arranca"
		else:
			print "No Arranca"

	@staticmethod
	def conducir(gasolina):
		if gasolina > 0:
			gasolina -= 1
			print "Quedan", gasolina, "litros"
		else:
			print "No se mueve..."
