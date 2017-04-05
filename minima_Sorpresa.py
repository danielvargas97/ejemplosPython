# -*- coding: cp1252 -*- #
#Principio de la mínima sorpresa#

class Operador():
    def mcd(self,a,b):
        #Se cumple la minima sorpresa porque hace lo que su nombre dice#
        while(b!=0):
            r= a%b
            a = b
            b = r
        return a



class OperadorMal():
    def mcd(self,a,b):
        #Segun el principio de minima sorpresa#
        #Debería retornar el maximo comun divisor de a y b#
        return a**b



if __name__ == "__main__":
    mcd = Operador()
    noMcd = OperadorMal()

    print("Maximo común divisor")
    x = int(input("Ingrese un numero:"))
    y = int(input("Ingrese un numero:"))

    
    #Imprimiendo la respuesta incorrecta#
    print("mcd("+str(x)+","+str(y)+"):"+str(noMcd.mcd(x,y)))

    #Imprimiendo la respuesta correcta
    print("mcd("+str(x)+","+str(y)+"):"+str(mcd.mcd(x,y)) )

    
    

    
    
