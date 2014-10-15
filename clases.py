class Auto:
    """Abstraccion a objeto de
    un auto, esta clase va a arrancar
    un auto, segun su nivel de gasolina"""
    def __init__(self, gasolina):
        self.gasolina = gasolina
        print "Tenemos", gasolina, "litros"
	
	
    def arrancar(self):
        if self.gasolina > 0:
            print "Arranca"
        else:
            print "No Arranca"


    def conducir(self):
        if self.gasolina > 0:
            self.gasolina -= 1
            print "Quedan", self.gasolina, "litros"
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
