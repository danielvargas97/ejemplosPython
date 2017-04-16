class OperacionVehiculo(object):
    def acelerar(self):
        pass
    def girar(self):
        pass

    def llenarTanque(self):
        pass

class Frenable(object):
    def frenar(self):
        pass



class Vehiculo(OperacionVehiculo,Frenable):
    def __init__(self):
        self.__matricula = "0"
        self.__color = ""
        self.__combustible = 0
        self.__velocidad = 0

    def getDatosVehiculo(self):
        print("Matricula: "+self.__matricula)
        print("Color: "+self.__color)
        print("Combustible: "+self.__combustible)



class Carro(Vehiculo,Frenable):
    def __init__(self,matricula,color):
        self.__matricula = matricula
        self.__color = color
        self.__combustible = 0
        self.__velocidad = 0
    
    def acelerar(self):
        if(self.__combustible <= 0):
            print ("El carro no puede andar porque no tiene combustible")
        else:
            while(self.__combustible >0):
                self.__velocidad = self.__velocidad + 5
                print( "Velocidad:"+str(self.__velocidad))
                self.__combustible = self.__combustible - 5

            

    def llenarTanque(self,cantidad):

        if(cantidad>0 and cantidad <=100):
            self.__combustible = cantidad


    def frenar(self):
        if(self.__velocidad ==0):
            print("El carro no está en movimiento")
        else:
            while(self.__velocidad !=0):
                self.__velocidad = self.__velocidad - 5
                print("Velocidad:"+str(self.__velocidad))

if __name__ == "__main__":
    toyota = Carro("ABC123","Rojo")
    #toyota.getDatosVehiculo()#
    toyota.llenarTanque(100)
    toyota.acelerar()#
    toyota.frenar()
    
    
        
