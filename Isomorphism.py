#-*- coding:utf-8 -*-#
#Isomorphism Example#

class Animal(object):
    def alimentar(self):
        pass
    def hacer_sonido(self):
        pass
    def mostrar_nombre(self):
        pass
    def mostrar_tipo(self):
        pass

class Perro(Animal):
    def __init__(self,nombre):
        self._tipo = "Perro"
        self._nombre = nombre
        self._sonido = "Wow Wow"
    def mostrar_tipo(self):
        return getattr(self,"_tipo")
    def mostrar_nombre(self):
        return getattr(self,"_nombre")
    def hacer_sonido(self):
        print (getattr(self,"_sonido"))
    def alimentar(self):
        print("Alimentado con Croquetas")



class Parque(object):
    def __init__(self):
        self._animal = []

    def crear_animal(self,nombre):
        c = Perro(nombre)

        self._animal.append(c)
            
    def main(self):
        print("Llenando el parque con animales")
        self.crear_animal("Fido")
        self.crear_animal("Lucas")
        self.crear_animal("Fido II")
        self.crear_animal("Fernando")

        for i in range(0,len(self._animal)):
            c = self._animal[i]
            print(c.mostrar_tipo()+":"+c.mostrar_nombre())
            c.hacer_sonido()
            c.alimentar()



if __name__ == "__main__":
    p = Parque()
    p.main()

