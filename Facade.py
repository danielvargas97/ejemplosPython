# -*- coding: cp1252 -*-
class Banio:
    def entrar(self):
        print("entrando al baño")
    def salir(self):
        print("saliendo del baño")

class Shampoo:
    def aplicar(self):
        print("aplicando shampoo")
    
class Jabon:
    def enjabonar(self):
        print("enjabonarse")

class Lavado:
    def lavar(self):
        print("aplicando agua")

class Aseo:
    def __init__(self):
        self.banio = Banio()
        self.jabon = Jabon()
        self.shampoo = Shampoo()
        self.lavado = Lavado()
        
    def baniarse(self):
        self.banio.entrar()
        self.lavado.lavar()
        self.shampoo.aplicar()
        self.jabon.enjabonar()
        self.lavado.lavar()

if __name__ == '__main__':
    fachada = Aseo()
    fachada.baniarse()
    
