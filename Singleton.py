class Caja(object):
    def __init__(self, nombre, monto):
        self.nombre = nombre
        self.monto = monto


Caja = Caja("A",50)


print(Caja.nombre)
