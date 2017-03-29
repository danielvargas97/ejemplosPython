#Ejemplo de Wrap#

class Pato(object):
    def __init__(self,sonido):
        self.sonido = sonido

    def getSonido(self):
        print(self.sonido)

class Estanque(object):
    def __init__(self,unPato):
        self.unPato = unPato

    def getSonido(self):
        self.unPato.getSonido()

    
if __name__ == "__main__":
    p = Pato("Quack")
    estanque = Estanque(p)
    estanque.getSonido()
    
