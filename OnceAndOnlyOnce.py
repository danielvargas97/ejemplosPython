#-*- coding:utf-8 -*-#
#EXAMPLE OF ONE AND ONLY ONCE#

from random import *

#Clase Abstracta#
class Personaje(object):
    
    def asignar_nombre(self, nombre):
        self.nombre = nombre
    def asignar_valores(self,vida,ataque):
        self.vida = vida
        self.ataque = ataque

    def asignar_tipo(self,tipo):
        self.tipo = tipo
        
    #Muestra la información basica del personaje#
    def ver_info(self):
        print(self.tipo)
        print("Nombre:"+str(self.nombre))
        print("Vida:"+str(self.vida))
        print("Ataque:"+str(self.ataque))
        print()

    def atacar(self,personaje):
        self.recibir_ataque(personaje,self.generar_ataque())
    
    #Muestra un ataque de prueba aleatorio#
    def generar_ataque(self):
        valor_ataque = randint(self.ataque//2,self.ataque)
        print("Valor del ataque:"+str(valor_ataque))
        print()
        return valor_ataque

    def recibir_ataque(self,personaje,valor_ataque):
        personaje.vida-=valor_ataque

#Clase Derivada - Humano#
class Humano(Personaje):
    def __init__(self,nombre,vida,ataque):
        super().asignar_tipo("Humano")
        super().asignar_valores(vida,ataque)
        super().asignar_nombre(nombre)


#Clase Derivada - Elfo#
class Elfo(Personaje):
    def __init__(self,nombre,vida,ataque):
        super().asignar_tipo("Elfo")
        super().asignar_valores(vida,ataque)
        super().asignar_nombre(nombre)


if __name__ == "__main__":
    soldado = Humano("Alain",100,25)
    arquero = Elfo("Pedro",200,15)
    
    #Viendo la info de los personajes#
    soldado.ver_info()
    arquero.ver_info()

    #Ataques#
    soldado.atacar(arquero)
    arquero.atacar(soldado)

    #Luego de los ataques#
    soldado.ver_info()
    arquero.ver_info()
