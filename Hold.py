#Ejemplo de Hold#

class Pato(object):
    def __init__(self,sonido):
        self.sonido = sonido

    def getSonido(self):
        print(self.sonido)

class Estanque(object):
    def __init__(self,unPato):
        self.unPato = unPato

    
if __name__ == "__main__":
    p = Pato("Quack")
    estanque = Estanque(p)
    estanque.unPato.getSonido()
    
