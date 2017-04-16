# -*- coding:utf-8 -*- #
#Substraction - Example#

#EJEMPLO de Substraccion#
#SE SUPONE QUE NO HAY NADA QUE AGREGAR NI NADA QUE QUITAR#
#DENTRO DEL DISEÑO#


from random import *

class MazoAbs(object):
    def revolver_mazo(self):
        pass
    def llenar_mazo(self):
        pass
    def ver_mazo(self):
        pass


class CartaAbs(object):
    def ver_info(self):
        pass
    def get_valor_carta(self):
        pass
    def crear_carta(self):
        pass
    
class Carta(CartaAbs):
    def __init__(self):
        self._nombre = ""
        self._valor = 0
        self._palo = ""
        

    def ver_info(self):
        print(getattr(self,"_nombre")+" "+getattr(self,"_palo"),'')
    
    def get_valor_carta(self):
        return getattr(self,"_valor")

    def crear_carta(self,nombre,palo):
        setattr(self,"_nombre", nombre)
        setattr(self,"_palo",palo)
        if nombre == "K" or nombre == "Q" or nombre =="J":
            setattr(self,"_valor",10)
        elif nombre == "A":
            setattr(self,"_valor",1)
        else:
            setattr(self,"_valor",int(nombre))

class Mazo(MazoAbs):
    def __init__(self):
        self.nombres=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        self.valores=[1,2,3,4,5,6,7,8,9,10]
        self.palos=["Diamante","Pica","Trébol","Corazón"]
        self.baraja = []

    def crear_baraja(self):
        self.llenar_mazo()
        self.revolver_mazo()

    def llenar_mazo(self):
        for i in range(0,len(self.palos)):
            for j in range(0,len(self.nombres)):
                miCarta = Carta()
                miCarta.crear_carta(self.nombres[j],self.palos[i])
                self.baraja.append(miCarta)

    def revolver_mazo(self):
        shuffle(self.baraja)

    def ver_mazo(self):
        for i in range(0,len(self.baraja)):
            c = self.baraja[i]
            c.ver_info()

    def get_carta(self,x):
        return self.baraja[x]

    def extrae_carta(self,x):
        self.baraja.pop(x)

    def get_cantidad(self):
        return len(self.baraja)

    def is_empty(self):
        if len(self.baraja)==0:
            return True
        else:
            return False

class Player(object):
    def __init__(self):
        self.rondas = 0
        self.ganados = 0

    def jugar(self):
        self.rondas+=1


    def contar_ganador(self):
        self.ganados+=1

class Juego(object):
    def __init__(self):
        self.player = Player()
        self.mazo = Mazo()
        self.mazo.crear_baraja()
        self.carta = None


    def pedir_carta(self):
        if not self.mazo.is_empty():
            cantidad = self.mazo.get_cantidad()-1
            indice = randint(0,cantidad)
            print("Hay "+str(cantidad+1)+" cartas")
            self.carta = self.mazo.get_carta(indice)
            self.mazo.extrae_carta(indice)
            return True
        else:
            print("Se acabaron las cartas!!!")
            return False

    def intro(self):
        print("Carta alta/baja")
        print("Escribe ALTA para pedir una carta alta")
        print("Escribe BAJA para pedir una carta baja")
        
    def check_str(self,cadena):
        if cadena == "ALTA" or cadena == "alta":
            return True
        if cadena == "BAJA" or cadena == "baja":
            return True
        return False

    def confirmar(self,cadena):
        return self.check_alta(cadena) or self.check_baja(cadena)
       
    def check_alta(self,cadena):
        valor_carta = self.carta.get_valor_carta()
        if cadena == "alta" and valor_carta>5:
            return True
        if cadena == "ALTA" and valor_carta()>5:
            return True
        return False

    def check_baja(self,cadena):
        valor_carta = self.carta.get_valor_carta()
        if cadena == "baja" and valor_carta<=5:
            return True
        if cadena == "BAJA" and valor_carta<=5:
            return True
        return False


    def iniciar(self):
        self.intro()
        self.mazo.ver_mazo()
        while True:
            self.player.jugar()
            x = input("Pide una carta:")
            while not self.check_str(x):
                print("No valido")
                x = input("Pide una carta:")
            if self.pedir_carta():
                self.carta.ver_info()
                if not self.confirmar(x):
                    print("Fin del Juego")
                    break
                self.player.contar_ganador()               
        print("Ganados:"+str(getattr(self.player,"ganados")))



if __name__ == "__main__":
    g = Juego()
    g.iniciar()
